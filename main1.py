import flet as ft

def main(page:ft.Page):
    #Configuração da página
    page.title = 'Miha aplicação flet'
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Definição de função
    def mostrar_nome(e):
        txt_resultado.value = f'{input_nome.value} {input_sobrenome.value}'
        page.update()

    #Criação de componentes
    input_nome = ft.TextField(label='Nome', hint_text= 'Digite seu nome')
    input_sobrenome = ft.TextField(label='Sobrenome', hint_text= 'Digite seu sobrenome')
    btn_enviar = ft.FilledButton(
        text='Enviar',
        width=page.window.width,
        on_click=mostrar_nome
    )
    txt_resultado = ft.Text(value='')


    #Contruir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,
                btn_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)