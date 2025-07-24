"""
menu_principal.py

Módulo responsável por exibir e controlar o menu principal da loja fictícia,
encaminhando o usuário para as funcionalidades de cadastros, pagamentos, catálogo
de produtos ou pedidos, com base na opção selecionada.

Funções:
- exibir_menu_principal(): Inicia e exibe o menu principal da aplicação.
- menu_cadastros(): Exibe o submenu relacionado às operações de cadastro de produtos.
"""

import cadastros
import pagamentos
import catalogo
import pedidos
import interface

def exibir_menu_principal():
    """
    Exibe o menu principal do sistema da loja, permitindo ao usuário
    navegar entre cadastros, pagamentos, catálogo e pedidos.

    A função permanece em loop até o usuário escolher sair.
    """
    while True:
        opcoes = [
            "Cadastros",
            "Pagamentos",
            "Catálogo de Produtos",
            "Pedidos",
            "Sair"
        ]
        interface.mostrar_menu(opcoes, "🏬 MENU PRINCIPAL")
        opcao = input()

        if opcao == "1":
            menu_cadastros()
        elif opcao == "2":
            pagamentos.realizar_pagamento()
        elif opcao == "3":
            catalogo.exibir_catalogo()
        elif opcao == "4":
            pedidos.menu_pedidos()
        elif opcao == "5":
            interface.limpar_tela()
            interface.mensagem_sucesso("👋 Obrigado por usar a loja!")
            break
        else:
            interface.mensagem_alerta("❌ Opção inválida.")
            interface.pausar()

def menu_cadastros():
    """
    Exibe o submenu de cadastros, permitindo ao usuário:
    - Cadastrar novo produto
    - Excluir um produto existente
    - Editar um produto
    - Voltar ao menu principal

    A função permanece em loop até o usuário optar por voltar.
    """
    while True:
        opcoes = [
            "Cadastrar Produto/Roupa",
            "Excluir Produto",
            "Editar Produto",
            "Voltar"
        ]
        interface.mostrar_menu(opcoes, "📦 MENU DE CADASTROS")
        opcao = input()

        if opcao == "1":
            cadastros.cadastrar_item()
        elif opcao == "2":
            cadastros.excluir_item()
        elif opcao == "3":
            cadastros.editar_item()
        elif opcao == "4":
            break
        else:
            interface.mensagem_alerta("❌ Opção inválida.")
            interface.pausar()
