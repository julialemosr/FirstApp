import flet as ft

def main(page:ft.Page):
    #Configuração da página
    page.title = 'Miha aplicação flet'
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Definição de função
    def adicao(e):
        soma = int(input_num1.value) + int(input_num2.value)
        txt_resultado.value = f"Resultado {soma}"
        page.update()

    def subtracao(e):
        subtracao = int(input_num1.value) - int(input_num2.value)
        txt_resultado.value = f"Resultado {subtracao}"
        page.update()

    def multiplicacao(e):
        multiplicacao = int(input_num1.value) * int(input_num2.value)
        txt_resultado.value = f"Resultado {multiplicacao}"
        page.update()

    def divisao(e):
        divisao = int(input_num1.value) / int(input_num2.value)
        txt_resultado.value = f"Resultado {divisao}"
        page.update()

    #Criação de componentes
    input_num1 = ft.TextField(label='Número 1', hint_text= 'Digite o primeiro número')
    input_num2 = ft.TextField(label='Número 2', hint_text= 'Digite o segundo número')

    btn_somar = ft.FilledButton(
        text='Somar',
        width=page.window.width,
        on_click=adicao
    )
    btn_subtracao = ft.FilledButton(
        text='Subtração',
        width=page.window.width,
        on_click=subtracao
    )
    btn_multiplicacao = ft.FilledButton(
        text='Multiplicação',
        width=page.window.width,
        on_click=multiplicacao
    )
    btn_divisao = ft.FilledButton(
        text='Divisão',
        width=page.window.width,
        on_click=divisao
    )
    txt_resultado = ft.Text(value='')


    #Contruir o layout
    page.add(
        ft.Column(
            [
                input_num1,
                input_num2,
                btn_somar,
                btn_subtracao,
                btn_multiplicacao,
                btn_divisao,
                txt_resultado,
            ]
        )
    )

ft.app(main)