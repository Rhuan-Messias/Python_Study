"""
Arquivo principal do sistema da loja fictícia.

Este script inicializa o sistema, exibindo o menu principal da aplicação
e registrando uma função de limpeza que apaga arquivos temporários ao final da execução.

Módulos Importados:
- menu_principal: Contém a lógica de exibição e controle do menu principal do sistema.
- manipulacaoArquivos: Responsável por operações com arquivos locais, como leitura, escrita e limpeza.
- atexit: Módulo da biblioteca padrão usado para registrar funções a serem chamadas ao encerrar o programa.

Uso:
Execute este script diretamente para iniciar o sistema.
"""

import menu_principal
import manipulacaoArquivos
import atexit

# Registra a função de limpeza automática ao sair do programa
atexit.register(manipulacaoArquivos.apagarArquivosTemporarios)

if __name__ == "__main__":
    # Inicia a interface principal do sistema
    menu_principal.exibir_menu_principal()
