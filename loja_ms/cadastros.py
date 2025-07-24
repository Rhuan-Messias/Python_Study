"""
cadastros.py

Módulo responsável pelo gerenciamento dos produtos cadastrados localmente.
Permite cadastrar novos itens (produto ou roupa), editar e excluir itens existentes.

Funções:
- cadastrar_item(): Cadastro de novos produtos ou roupas.
- gerar_id_produto(): Gera um novo ID único baseado nos produtos locais.
- excluir_item(): Remove um produto da lista local com base no ID.
- editar_item(): Atualiza nome, preço ou descrição de um produto existente.
"""

import manipulacaoArquivos
import interface

def cadastrar_item():
    """
    Solicita dados do usuário para cadastrar um novo item (produto ou roupa),
    atribui um ID automático e salva o item no arquivo local.

    Exibe mensagens de sucesso ou alerta conforme a operação.
    """
    interface.limpar_tela()
    interface.titulo("📋 Cadastro de Produtos/Roupas")

    tipo = input("Cadastrar (1) Produto ou (2) Roupa? ")

    if tipo in ["1", "2"]:
        nome = input("Nome: ")
        preco = float(input("Preço: R$ "))
        descricao = input("Descrição: ")
        id_fake = gerar_id_produto()
        manipulacaoArquivos.gravarProdutoFakeStore(id_fake, nome, preco, descricao)
        tipo_nome = "Produto" if tipo == "1" else "Roupa"
        interface.mensagem_sucesso(f"✅ {tipo_nome} '{nome}' cadastrado com sucesso.")
    else:
        interface.mensagem_alerta("❌ Opção inválida.")
    
    interface.pausar()

def gerar_id_produto():
    """
    Gera um novo ID único para produto com base no maior ID existente nos produtos locais.

    Retorna:
        int: Novo ID disponível (inicia em 21 se não houver produtos).
    """
    produtos_locais = manipulacaoArquivos.lerProdutosLocais()
    return max(p['id'] for p in produtos_locais) + 1 if produtos_locais else 21

def excluir_item():
    """
    Lista os produtos locais e permite ao usuário excluir um deles com base no ID informado.

    Solicita confirmação antes da exclusão e salva o novo estado do arquivo após a remoção.
    Emite mensagens para sucesso, cancelamento ou erro.
    """
    interface.limpar_tela()
    produtos = manipulacaoArquivos.lerProdutosLocais()

    if not produtos:
        interface.mensagem_alerta("⚠️ Nenhum produto local para excluir.")
        interface.pausar()
        return

    interface.titulo("🗑️ Exclusão de Produtos Locais")
    interface.mostrar_tabela_produtos(produtos)

    try:
        id_excluir = int(input("Digite o ID do produto que deseja excluir: "))
        produto = next((p for p in produtos if p['id'] == id_excluir), None)

        if not produto:
            interface.mensagem_alerta("❌ Produto não encontrado.")
            interface.pausar()
            return

        confirmacao = input(f"Tem certeza que deseja excluir '{produto['title']}'? [S/N]: ").strip().upper()
        if confirmacao != "S":
            interface.mensagem_alerta("❌ Exclusão cancelada.")
            interface.pausar()
            return

        produtos = [p for p in produtos if p['id'] != id_excluir]
        with open("produtos_local.txt", "w") as f:
            for p in produtos:
                f.write(f"{p['id']};{p['title']};{p['price']};{p['description']}\n")

        interface.mensagem_sucesso("✅ Produto excluído com sucesso.")
    except ValueError:
        interface.mensagem_alerta("❌ Entrada inválida.")

    interface.pausar()

def editar_item():
    """
    Permite editar os dados (nome, preço e descrição) de um produto local baseado no ID.

    Mantém os valores antigos caso o usuário pressione ENTER sem digitar um novo valor.
    Salva o novo estado no arquivo local.
    """
    interface.limpar_tela()
    produtos = manipulacaoArquivos.lerProdutosLocais()

    if not produtos:
        interface.mensagem_alerta("⚠️ Nenhum produto local para editar.")
        interface.pausar()
        return

    interface.titulo("🛠️ Edição de Produtos Locais")
    interface.mostrar_tabela_produtos(produtos)

    try:
        id_editar = int(input("Digite o ID do produto que deseja editar: "))
        produto = next((p for p in produtos if p['id'] == id_editar), None)

        if not produto:
            interface.mensagem_alerta("❌ Produto não encontrado.")
            interface.pausar()
            return

        novo_nome = input(f"Novo nome ({produto['title']}): ") or produto['title']
        novo_preco = input(f"Novo preço ({produto['price']}): ")
        novo_preco = float(novo_preco) if novo_preco.strip() else produto['price']
        nova_desc = input(f"Nova descrição ({produto['description']}): ") or produto['description']

        produto['title'] = novo_nome
        produto['price'] = novo_preco
        produto['description'] = nova_desc

        with open("produtos_local.txt", "w") as f:
            for p in produtos:
                f.write(f"{p['id']};{p['title']};{p['price']};{p['description']}\n")

        interface.mensagem_sucesso("✅ Produto atualizado com sucesso.")
    except ValueError:
        interface.mensagem_alerta("❌ Entrada inválida.")

    interface.pausar()
