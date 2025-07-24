"""
catalogo.py

Este módulo lida com a exibição do catálogo de produtos da loja.
Ele acessa a Fake Store API e combina os produtos obtidos com os produtos
salvos localmente, permitindo a visualização do catálogo completo
ou apenas dos produtos promocionais (preço < R$60).

Módulos utilizados:
- requests: para acessar dados da Fake Store API.
- manipulacaoArquivos: para carregar produtos salvos localmente.
- interface: para exibição de mensagens e interface no terminal.

Funções:
- exibir_catalogo(): Exibe o catálogo de produtos com ou sem filtro promocional.
"""

import requests
import manipulacaoArquivos
import interface

def exibir_catalogo():
    """
    Exibe o catálogo de produtos ao usuário, com opção de visualizar apenas produtos promocionais.

    O catálogo é formado por:
    - Produtos obtidos da Fake Store API.
    - Produtos salvos localmente.

    Se o usuário escolher ver o catálogo promocional, apenas produtos com
    preço abaixo de R$60 serão exibidos.

    Em caso de erro na API, apenas os produtos locais serão usados.

    Returns:
        None
    """
    interface.limpar_tela()
    interface.titulo("🛍️ CATÁLOGO DE PRODUTOS")
    promocao = input("Deseja ver o catálogo promocional (preço < R$60)? [S/N]: ").strip().upper()

    try:
        res = requests.get("https://fakestoreapi.com/products")
        produtos_api = res.json() if res.status_code == 200 else []
    except:
        interface.mensagem_alerta("❌ Erro ao acessar a Fake Store API.")
        produtos_api = []

    produtos_locais = manipulacaoArquivos.lerProdutosLocais()
    todos_produtos = produtos_api + produtos_locais

    filtrados = [p for p in todos_produtos if p["price"] < 60] if promocao == "S" else todos_produtos

    interface.mostrar_tabela_produtos(filtrados)
    interface.pausar()
