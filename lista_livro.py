import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class user():
    def __init__(self, titulo,descricao,categoria, autor):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor

def main(page: ft.Page):
    page.title = "Lista de Livro"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    lista = []
    def salvar_titulo(e):
        if input_titulo.value == '' or input_descricao.value == '' or input_categoria.value == '' or input_autor.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            obj_user = user(
                titulo=input_titulo.value,
                descricao= input_descricao.value,
                categoria= input_categoria.value,
                autor= input_autor.value,
            )
            lista.append(obj_user)
            input_titulo.value = ''
            input_descricao.value = ''
            input_categoria.value = ''
            input_autor.value = ''
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_titulo.controls.clear()
        for livro in lista:
            lv_titulo.controls.append(
                ft.Text(value=f"{livro.titulo} - {livro.descricao} - {livro.categoria} - {livro.autor}"),
            )
        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_titulo(e)
                    ),
                    ft.Button(
                        text="Exibir lista de livro",
                        on_click= lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)

            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Resultado livros"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_titulo,

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    msg_sucesso = ft.SnackBar(
        content=ft.Text('Campos preenchidos com sucesso'),
        bgcolor=Colors.GREEN,
    )

    msg_error = ft.SnackBar(
        content=ft.Text('Os campos não podem estar vazio'),
        bgcolor=Colors.RED,
    )

    input_titulo = ft.TextField(label='Título')
    input_descricao = ft.TextField(label='Descrição')
    input_categoria = ft.TextField(label='Categoria')
    input_autor = ft.TextField(label='Autor')

    lv_titulo = ft.ListView(
        height=500
    )

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)