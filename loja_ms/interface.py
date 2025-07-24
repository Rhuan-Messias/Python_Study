"""
módulo: interface.py

Este módulo é responsável pela interface visual da loja no terminal,
utilizando a biblioteca `rich` para formatar a saída com painéis,
tabelas, cores e estilos.

Funcionalidades oferecidas:
- Limpeza da tela.
- Exibição de título com painel.
- Menus interativos com opções numeradas.
- Exibição de produtos e pedidos em formato de tabela.
- Mensagens de sucesso ou alerta.
- Pausa para interação do usuário.

Este módulo é utilizado por outras partes do sistema como menu_principal,
cadastros, pedidos e pagamentos, fornecendo uma camada visual unificada.
"""

import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def limpar_tela():
    """
    Limpa a tela do terminal, usando 'cls' no Windows e 'clear' no Linux/macOS.
    """
    os.system("cls" if os.name == "nt" else "clear")

def titulo(texto):
    """
    Exibe um título estilizado com borda, utilizando painel colorido da biblioteca rich.

    Parâmetros:
    - texto (str): O texto que será exibido como título principal.
    """
    panel = Panel.fit(
        f"[bold cyan]{texto}[/bold cyan]",
        border_style="cyan",
        padding=(1, 4),
        title="🛍️ Nova Loja em Microsserviços",
        subtitle="Tópicos de Eng. de Software"
    )
    console.print(panel)

def mostrar_menu(opcoes, titulo_menu="MENU"):
    """
    Exibe um menu interativo com opções numeradas.

    Parâmetros:
    - opcoes (list[str]): Lista de opções a serem mostradas.
    - titulo_menu (str): Título do menu (opcional, padrão: "MENU").
    """
    limpar_tela()
    titulo(titulo_menu)
    for i, opcao in enumerate(opcoes, 1):
        console.print(f"[green]{i}[/green] - {opcao}")
    console.print("[yellow]Escolha uma opção: [/yellow]", end="")

def mostrar_tabela_produtos(produtos):
    """
    Exibe os produtos disponíveis em formato de tabela.

    Parâmetros:
    - produtos (list[dict]): Lista de dicionários com os produtos.
      Cada produto deve conter as chaves: 'id', 'title' e 'price'.
    """
    table = Table(title="📦 Produtos Disponíveis", header_style="bold magenta")
    table.add_column("ID", justify="center")
    table.add_column("Nome")
    table.add_column("Preço (R$)", justify="right")

    for p in produtos:
        table.add_row(str(p["id"]), p["title"], f"R$ {p['price']:.2f}")

    console.print(table)

def mostrar_tabela_pedidos(pedidos):
    """
    Exibe os itens adicionados ao pedido em formato de tabela.

    Parâmetros:
    - pedidos (list[tuple]): Lista de tuplas no formato (id, nome, preco).
    """
    table = Table(title="🧾 Itens no Pedido", header_style="bold yellow")
    table.add_column("#", justify="center")
    table.add_column("Nome")
    table.add_column("Preço (R$)", justify="right")

    for i, item in enumerate(pedidos, 1):
        table.add_row(str(i), item[1], f"R$ {item[2]:.2f}")

    console.print(table)

def mensagem_alerta(texto):
    """
    Exibe uma mensagem de alerta em vermelho.

    Parâmetros:
    - texto (str): Mensagem a ser exibida.
    """
    console.print(f"[bold red]{texto}[/bold red]")

def mensagem_sucesso(texto):
    """
    Exibe uma mensagem de sucesso em verde.

    Parâmetros:
    - texto (str): Mensagem a ser exibida.
    """
    console.print(f"[bold green]{texto}[/bold green]")

def pausar():
    """
    Pausa a execução até que o usuário pressione Enter.
    Utilizado para dar tempo de leitura ao usuário.
    """
    console.print("\n[dim]Pressione [bold]Enter[/bold] para continuar...[/dim]")
    input()
