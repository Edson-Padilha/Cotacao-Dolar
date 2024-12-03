import flet as ft 
import requests

def main(page: ft.Page):
    page.title = "Cotação do Dólar"

    def get_dolar_quotation():
        try:
            response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
            response.raise_for_status() # Verfica se a requisição foi bem sucedida
            data = response.json()
            cotacao = data['USDBRL']['bid']
            return cotacao
        
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

    def update_quotation(e):
        cotacao = get_dolar_quotation()
        if cotacao:
            texto_cotacao.value = f"Dólar: R$ {cotacao}"
        else:
            texto_cotacao.value = f"Erro ao obter cotação"
        page.update()

    texto_cotacao = ft.Text("Cotação do Dólar: ", size=20)
    botao_atualizar = ft.ElevatedButton("Atualizar", on_click=update_quotation)

    page.add(texto_cotacao, botao_atualizar)
ft.app(target=main)