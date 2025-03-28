import flet as ft
from datetime import datetime


def main(page:ft.Page):
    #Configuração da página
    page.title = 'Miha aplicação flet'
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Definição de função
    def mostrar_idade(e):
        txt_resultado.value = input_nascimento.value
        data_nascimento = datetime.strptime(input_nascimento.value, '%d/%m/%Y')
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year
        if datetime.today().month < data_nascimento.month:
            idade = idade - 1
        if int(idade)  >= 18:
            txt_resultado.value = f'Maior de idade'
        else:
            txt_resultado.value = f'Menor de idade'

        page.update()

    #Criação de componentes
    input_nascimento = ft.TextField(label='Nascimento', hint_text= 'Data de Nascimento')
    btn_enviar = ft.FilledButton(
        text='Enviar',
        width=page.window.width,
        on_click=mostrar_idade,
    )
    txt_resultado = ft.Text(value='')


    #Contruir o layout
    page.add(
        ft.Column(
            [
                input_nascimento,
                btn_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)