import flet as ft 
import requests
import time

def main(page: ft.Page):
    page.title = "Cotação do Dólar"

    def get_dolar_quotation():
        try:
            response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
            response.raise_for_status() # Verfica se a requisição foi bem sucedida
            data = response.json()
            return data['USDBRL']
        
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

    
    texto_cotacao = ft.Text("Cotação do Dólar: ", size=20)
    texto_maxima = ft.Text(f"Máxima do dia: ", size=20) 
    texto_minima = ft.Text(f"Mínima do dia: ", size=20)

    def update_quotation():
        data = get_dolar_quotation()

        if data:
            texto_cotacao.value = f"Dólar: R$ {data['bid']}"
            texto_maxima.value = f"Máxima do dia: R$ {data['high']}"
            texto_minima.value = f"Mínima do dia: R$ {data['low']}"
        
        else:
            texto_cotacao.value = f"Erro ao obter cotação"
        page.update()
    
    def timer_tick(e):
        update_quotation()
        
    update_quotation()

    # Configura o timer para chamar update_quotation a cada 1 segundo
    page.on_show = lambda e: page.add(ft.Timer(1, on_tick=timer_tick))

    page.add(texto_cotacao, texto_maxima, texto_minima)
ft.app(target=main)