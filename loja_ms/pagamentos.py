"""
pagamentos.py

Módulo responsável por processar os pedidos salvos e realizar o pagamento.
Calcula o valor total dos pedidos e permite selecionar a forma de pagamento.

Funções:
- realizar_pagamento(): Calcula o valor total e processa o pagamento,
  limpando o arquivo de pedidos após a quitação.
"""

import manipulacaoArquivos
import json
import interface

def realizar_pagamento():
    """
    Lê o arquivo de pedidos ("Pedidos.txt"), calcula o valor total acumulado
    e solicita ao usuário a forma de pagamento (crédito, débito ou dinheiro).

    Após o pagamento, o arquivo de pedidos é zerado, simulando a finalização da compra.

    Exibe mensagens de erro se o arquivo estiver ausente ou corrompido.
    """
    interface.limpar_tela()
    interface.titulo("💳 PAGAMENTO DE PEDIDOS")

    try:
        # Lê todas as linhas do arquivo de pedidos
        arquivo = manipulacaoArquivos.lerArquivo("Pedidos.txt", "r")
        pedidos = arquivo.readlines()
        arquivo.close()

        if not pedidos:
            interface.mensagem_alerta("⚠️ Nenhum pedido encontrado.")
            interface.pausar()
            return

        soma = 0.0
        # Processa cada linha e acumula o valor total dos itens
        for linha in pedidos:
            try:
                partes = linha.strip().split(";", 1)
                if len(partes) < 2:
                    continue
                lista = json.loads(partes[1])
                for item in lista:
                    soma += float(item["preco"])
            except Exception as e:
                interface.mensagem_alerta(f"Erro ao processar linha: {linha} → {e}")

        print(f"\n🧾 Valor total dos pedidos: R$ {soma:.2f}")
        metodo = input("💰 Forma de pagamento (crédito/débito/dinheiro): ")
        interface.mensagem_sucesso(f"✅ Pagamento de R$ {soma:.2f} realizado via {metodo.upper()}!")

        # Zera o conteúdo do arquivo após pagamento
        with open("Pedidos.txt", "w") as f:
            f.truncate()

        interface.mensagem_sucesso("🧾 Pedidos quitados e arquivo zerado.")
    except FileNotFoundError:
        interface.mensagem_alerta("❌ Arquivo de pedidos não encontrado.")
    
    interface.pausar()
