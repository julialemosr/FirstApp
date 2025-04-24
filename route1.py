import flet as ft
from flet import AppBar,ElevatedButton, Page,  Text, colors
from flet.core.colors import Colors
from flet.core.view import View


def main(page:ft.Page):
    #Configuração da página
    page.title = 'Exemplos de rotas'
    page.theme_mode = ft.ThemeMode.DARK #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda"))
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY),
                        Text (f"Olá {input_nome.value}, seja bem vindo!")
                    ]
                )
            )

        page.update()

    input_nome = ft.TextField(label='Nome', hint_text='Digite seu nome')


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)

