from datetime import datetime
import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, colors
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.view import View


def main(page: ft.Page):
    # Configuração da página
    page.title = 'simulador de aposentadoria'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Seja bem vindo ao INSS!"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text="Simulador de aposentadoria", on_click=lambda _: page.go("/segunda")),
                    ElevatedButton(text="Ver regras do simulador", on_click=lambda _: page.go("/terceira")),
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Simulador"), bgcolor=Colors.SECONDARY),
                        Text(f"SIMULADOR:"),
                        input_idade,
                        sexo,
                        input_contribuicao,
                        input_media_salarial,
                        categoria,
                        ElevatedButton(text="Simular aposentadoria", on_click=lambda _: page.go("/quarta"))
                    ]
                )
            )

        if page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Regras"), bgcolor=Colors.TERTIARY),
                        Text(f"REGRAS DO SIMULADOR:\n"),
                        Text(f"Aposentadoria por Idade:\n"),
                        Text(f"Homens: 65 anos de idade e pelo menos 15 anos de contribuição.\n"),
                        Text(f"Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n"),
                        Text(f"Aposentadoria por Tempo de Contribuição:\n"),
                        Text(f"Homens: 35 anos de contribuição.\n"),
                        Text(f"Mulheres: 30 anos de contribuição.\n"),
                        Text(f"Valor Estimado do Benefício:\n"),
                        Text(
                            f" O valor da aposentadoria será uma média de 60% da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimo  de contribuição. "),
                    ]
                )
            )

        if page.route == "/quarta":
            page.views.append(
                View(
                    "/quarta",
                    [
                        AppBar(title=Text("Resultado da simulação"), bgcolor=Colors.TERTIARY),
                        Text(f"RESULTADO:\n"),
                        genero(e),
                    ]
                )
            )

        page.update()

    input_idade = ft.TextField(label='Idade', hint_text='Digite sua idade atual')
    sexo = ft.Dropdown(
        label='Sexo',
        options=[Option('Masc', 'Masculino'), Option('Fem', 'Feminino')],
    )
    input_contribuicao = ft.TextField(label='Anos de contribuicao',
                                      hint_text='A quantos anos você contribui para o INSS')
    input_media_salarial = ft.TextField(label='Média salarial', hint_text='Média salarial dos últimos 5 anos')
    categoria = ft.Dropdown(
        label='Categoria de aposentadoria',
        options=[Option('Contribuicao', 'Aposentadoria por tempo de contribuição'),
                 Option('Idade', 'Aposentadoria por idade')],
    )

    def genero(e):

        # calc fem
        if categoria.value == 'Idade':
            if sexo.value == 'Fem':
                if int(input_idade.value) >= 62 and input_contribuicao.value == 15:
                    aposentadoria_i = (float(input_media_salarial.value) * 0.6)
                    Text.value = f'Você já pode se aposentar e irá receber R${aposentadoria_i} de aposentadoria.'

                elif int(input_idade.value) >= 62 and int(input_contribuicao.value) > 15:
                    aposentadoria_tc = (float(input_media_salarial.value) * 0.6)
                    diferenca = int(input_contribuicao.value) - 15
                    extra = diferenca * 0.2
                    total_aposentadoria_tc = aposentadoria_tc + extra
                    Text.value = f'Você já pode se aposentar e irá receber R${total_aposentadoria_tc} de aposentadoria.'
                else:
                    ano_atual = datetime.now().year
                    data_aposentadoria = (int(input_idade.value) - 62) + ano_atual
                    Text.value = f'Você ainda não pode se aposentar, mas poderá se aposentar em {data_aposentadoria}.'

            else:
                if int(input_idade.value) >= 65 and input_contribuicao.value == 15:
                    aposentadoria_i = (float(input_media_salarial.value) * 0.6)
                    Text.value = f'Você já pode se aposentar e irá receber R${aposentadoria_i} de aposentadoria.'

                elif int(input_idade.value) >= 65 and int(input_contribuicao.value) > 15:
                    aposentadoria_tc = (float(input_media_salarial.value) * 0.6)
                    diferenca = int(input_contribuicao.value) - 15
                    extra = diferenca * 0.2
                    total_aposentadoria_tc = aposentadoria_tc + extra
                    Text.value = f'Você já pode se aposentar e irá receber R${total_aposentadoria_tc} de aposentadoria.'
                else:
                    ano_atual = datetime.now().year
                    data_aposentadoria = (int(input_idade.value) - 65) + ano_atual
                    Text.value = f'Você ainda não pode se aposentar, mas poderá se aposentar em {data_aposentadoria}.'

        else:
            if sexo.value == 'Fem':
                if int(input_contribuicao.value) == 30:
                    aposentadoria_tc = (float(input_media_salarial.value) * 0.6)
                    Text.value = f'Você já pode se aposentar e irá receber R${aposentadoria_tc} de aposentadoria.'

                elif int(input_idade.value) > 30:
                    aposentadoria_tc = (float(input_media_salarial.value) * 0.6)
                    diferenca = int(input_contribuicao.value) - 15
                    extra = diferenca * 0.2
                    total_aposentadoria_tc = aposentadoria_tc + extra
                    Text.value = f'Você já pode se aposentar e irá receber R${total_aposentadoria_tc} de aposentadoria.'
                else:
                    ano_atual = datetime.now().year
                    data_aposentadoria = (int(input_contribuicao.value) - 30) + ano_atual
                    Text.value = f'Você ainda não pode se aposentar, mas poderá se aposentar em {data_aposentadoria}.'

            else:
                if int(input_contribuicao.value) == 35:
                    aposentadoria_tc = (float(input_media_salarial.value) * 0.6)
                    Text.value = f'Você já pode se aposentar e irá receber R${aposentadoria_tc} de aposentadoria.'

                elif int(input_idade.value) > 35:
                    aposentadoria_tc = (float(input_media_salarial.value) * 0.6)
                    diferenca = int(input_contribuicao.value) - 15
                    extra = diferenca * 0.2
                    total_aposentadoria_tc = aposentadoria_tc + extra
                    Text.value = f'Você já pode se aposentar e irá receber R${total_aposentadoria_tc} de aposentadoria.'
                else:
                    ano_atual = datetime.now().year
                    data_aposentadoria = (int(input_contribuicao.value) - 35) + ano_atual
                    Text.value = f'Você ainda não pode se aposentar, mas poderá se aposentar em {data_aposentadoria}.'

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

    page.go(page.route)


ft.app(main)
