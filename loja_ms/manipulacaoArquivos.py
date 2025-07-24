"""
manipulacaoArquivos.py

Módulo responsável pelo armazenamento local de dados da loja fictícia,
como produtos e pedidos, além de limpeza automática de arquivos temporários.

Funções:
- gravarProdutoFakeStore(): Salva um produto localmente.
- lerProdutosLocais(): Lê os produtos salvos localmente.
- gravarPedidos(): Armazena os pedidos feitos com data e hora.
- lerArquivo(): Abre um arquivo com o modo especificado.
- apagarArquivosTemporarios(): Remove arquivos temporários utilizados pela aplicação.
"""

import os
import json
from datetime import datetime

def gravarProdutoFakeStore(id, title, price, description):
    """
    Grava um produto em um arquivo local ("produtos_local.txt"), simulando
    persistência para produtos oriundos da Fake Store API.

    Parâmetros:
        id (int): ID do produto.
        title (str): Nome/título do produto.
        price (float): Preço do produto.
        description (str): Descrição do produto.
    """
    with open("produtos_local.txt", "a") as f:
        f.write(f"{id};{title};{price};{description}\n")

def lerProdutosLocais():
    """
    Lê o arquivo de produtos locais ("produtos_local.txt") e retorna uma
    lista de dicionários com os produtos armazenados.

    Retorna:
        list[dict]: Lista de produtos com campos 'id', 'title', 'price' e 'description'.
    """
    try:
        with open("produtos_local.txt", "r") as f:
            produtos = []
            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) == 4:
                    id_, title, price, description = partes
                    produtos.append({
                        "id": int(id_),
                        "title": title,
                        "price": float(price),
                        "description": description
                    })
            return produtos
    except FileNotFoundError:
        return []

def gravarPedidos(listaPedido, datahora):
    """
    Grava uma lista de itens de pedido com o horário da compra no arquivo "Pedidos.txt".

    Parâmetros:
        listaPedido (list[tuple]): Lista de tuplas com (id, nome, preco) de cada item.
        datahora (str): Data e hora da realização do pedido (formato livre).
    """
    # Convertemos para lista de dicts para evitar problemas com json.dumps em tuplas
    lista_dict = [{"id": item[0], "nome": item[1], "preco": item[2]} for item in listaPedido]
    with open("Pedidos.txt", "a") as f:
        f.write(f"{datahora};{json.dumps(lista_dict)}\n")

def lerArquivo(nome, modo="r"):
    """
    Abre um arquivo genérico com o nome e modo especificado.

    Parâmetros:
        nome (str): Nome do arquivo a ser aberto.
        modo (str): Modo de abertura ('r', 'w', 'a', etc.).

    Retorna:
        file object: Objeto de arquivo aberto.
    """
    return open(nome, modo)

def apagarArquivosTemporarios():
    """
    Remove os arquivos temporários criados localmente pela aplicação:
    - produtos_local.txt
    - Pedidos.txt

    Usado no encerramento automático da aplicação.
    """
    for arquivo in ["produtos_local.txt", "Pedidos.txt"]:
        if os.path.exists(arquivo):
            os.remove(arquivo)
