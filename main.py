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

    
    texto_cotacao = ft.Text("Cotação do Dólar: ", size=20, color=ft.colors.BLACK)
    texto_maxima = ft.Text(f"Máxima do dia: ", size=20, color=ft.colors.BLACK) 
    texto_minima = ft.Text(f"Mínima do dia: ", size=20, color=ft.colors.BLACK)
    texto_venda = ft.Text(f"Valor de venda: ", size=20, color=ft.colors.BLACK)

    def update_quotation(e=None):
        data = get_dolar_quotation()

        if data:
            texto_cotacao.value = f"Dólar: R$ {data['bid']}"
            texto_maxima.value = f"Máxima do dia: R$ {data['high']}"
            texto_minima.value = f"Mínima do dia: R$ {data['low']}"
            texto_venda.value = f"Valor de venda: R$ {data['ask']}"
        
        else:
            texto_cotacao.value = f"Erro ao obter cotação"
        
        # Atualiza o card com as novas informações
        card.content = ft.Container(
            content=ft.Column(
                [
                    texto_cotacao,
                    texto_maxima,
                    texto_minima,
                    texto_venda,
                ],
                alignment=ft.alignment.center,
            ),
            padding=10,
        )
        page.update()
    
    botao_atualizar = ft.ElevatedButton("Atualizar", on_click=update_quotation, bgcolor="green", color=ft.colors.WHITE)
    
    # Cria o card
    card = ft.Card(
        color=ft.colors.WHITE,
        content=ft.Container(
            content=ft.Column(
                [
                    texto_cotacao,
                    texto_maxima,
                    texto_minima,
                    texto_venda,
                ],
                alignment=ft.alignment.center,
            ),
            padding=10,
        )
    )
        
    update_quotation()

    page.add(
        ft.Column(
            [card,
            ft.Row([botao_atualizar], alignment=ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)