import flet as ft
from flet import AppBar, Text, View, ElevatedButton
from flet.core.colors import Colors
from sqlalchemy import select
from listview_bancodados.models import *


def main(page: ft.Page):
    page.title = "Livros"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    livros = []

    def salvar_livro(e):
        if input_nome.value == "" or input_autor.value == "" or input_descricao.value == "" or input_descricao.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
        else:
            livro = Livro(
                titulo=input_nome.value,
                autor=input_autor.value,
                descricao=input_descricao.value,
                categoria=input_categoria.value,
            )
            livro.save()
            input_nome.value = ""
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_livro.controls.clear()

        book = select(Livro)
        livros = db_session.execute(book).scalars().all()

        for l in livros:
            lv_livro.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.BOOK),
                    title=ft.Text(l.titulo),
                    subtitle=ft.Text(l.autor),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(
                                text="Detalhes do livro"
                            ),
                        ],
                        on_select=lambda _, liv=l: ver_detalhes(liv.titulo, liv.autor, liv.descricao, liv.categoria),
                    )

                )
            )
        page.update()

    def ver_detalhes(titulo, autor, descricao, categoria):
        txt.value = (f"Titulo: {titulo};"
                     f" \nAutor: {autor}; "
                     f"\nDescrição: {descricao}; "
                     f"\nCategoria: {categoria}.")
        page.go("/listar_detalhes")

    def gerencia_rota(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro de Livros"), bgcolor=Colors.PINK_200),
                    input_nome,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(text="Salvar Livro", on_click=salvar_livro, color=ft.CupertinoColors.SYSTEM_BACKGROUND, width=375),
                    ElevatedButton(text="Exibir a Lista", on_click=lambda _: page.go("/lista"), color=ft.CupertinoColors.SYSTEM_BACKGROUND, width=375),
                ]
            )
        )
        if page.route == "/lista":
            exibir_lista(e)
            page.views.append(
                View(
                    "/lista",
                    [
                        AppBar(title=Text("Lista de Livros."), bgcolor=Colors.PINK_200),
                        lv_livro
                    ]
                )
            )

        if page.route == "/lista_dos_detalhes":
            page.views.append(
                View(
                    "/lista_dos_detalhes",
                    [
                        AppBar(title=Text("Lista dos Livros"), bgcolor=Colors.PINK_200),
                        txt,
                        ElevatedButton(text="Voltar!", on_click=lambda _: page.go("/lista"), color=ft.CupertinoColors.SYSTEM_BACKGROUND, width=375)
                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Campos
    input_nome = ft.TextField(label="Titulo")
    input_descricao = ft.TextField(label="Descrição")
    input_categoria = ft.TextField(label="Categoria")
    input_autor = ft.TextField(label="Autor")
    txt = ft.Text(value="")
    lv_livro = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1,
    )

    msg_sucesso = ft.SnackBar(content=Text("Livro cadastrado com sucesso!"), bgcolor=Colors.GREEN)
    msg_erro = ft.SnackBar(content=Text("Não deixe os campos vazios!"), bgcolor=Colors.RED)

    page.overlay.append(msg_sucesso)
    page.overlay.append(msg_erro)
    page.on_route_change = gerencia_rota
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)