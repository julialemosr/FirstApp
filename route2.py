import flet as ft
from flet import AppBar,ElevatedButton, Page,  Text, View, colors
from flet.core import page
from flet.core.colors import Colors


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
                    AppBar(title=Text("Cadastro de livro"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
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
                        Text (f"Título do livro: {input_titulo.value}."),
                        Text (f"Descrição do livro: {input_descricao.value}."),
                        Text (f"Categoria do livro: {input_categoria.value}."),
                        Text (f"Autor do livro: {input_autor.value}.")
                    ]
                )
            )

        page.update()

    input_titulo = ft.TextField(label='Título', hint_text='Digite o título do livro')
    input_descricao = ft.TextField(label='Descrição', hint_text='Digite a descrição do livro')
    input_categoria = ft.TextField(label='Categoria', hint_text='Digite a categoria do livro')
    input_autor = ft.TextField(label='Autor', hint_text='Digite o autor do livro')


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)