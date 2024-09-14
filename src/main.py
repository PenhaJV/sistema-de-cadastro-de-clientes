from interface_usuario import *
from manipulacao_dados import *
import os


def limpar_tela():
    os.system("cls || clear")

def press_tecla_para_continuar():
    input("\nPressione ENTER tecla para continuar...")


def main():
    # Função principal para coordenar o fluxo do programa
    while True:
        limpar_tela()
        escolha = exibir_menu()

        if escolha == "1":
            limpar_tela()
            add_cliente()
            press_tecla_para_continuar()
        elif escolha == "2":
            limpar_tela()
            editar_cliente()
            press_tecla_para_continuar()
        elif escolha == "3":
            limpar_tela()
            listar_clientes()
            press_tecla_para_continuar()
        elif escolha == "4":
            limpar_tela()
            excluir_cliente()
            press_tecla_para_continuar()
        elif escolha == "5":
            limpar_tela()
            gerar_relatorio_clientes_cadastrados()
            press_tecla_para_continuar()
        elif escolha == "6":
            limpar_tela()
            print("Saindo...")
            press_tecla_para_continuar()
            break
        else:
            press_tecla_para_continuar()


if __name__ == "__main__":
    main()
