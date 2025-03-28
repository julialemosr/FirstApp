import flet as ft

def main(page:ft.Page):
    #Configuração da página
    page.title = 'Miha aplicação flet'
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Definição de função
    def verificar_numero(e):
        txt_resultado.value = {input_numero.value}
        numero = int(input_numero.value)
        par_impar = numero % 2
        if par_impar == 0:
            txt_resultado.value = f'O número é par'
        else:
            txt_resultado.value = f'O número é ímpar'

        page.update()


    #Criação de componentes
    input_numero = ft.TextField(label='Número', hint_text= 'Digite um número ')
    btn_enviar = ft.FilledButton(
        text='Enviar',
        width=page.window.width,
        on_click=verificar_numero,
    )
    txt_resultado = ft.Text(value='')


    #Contruir o layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)