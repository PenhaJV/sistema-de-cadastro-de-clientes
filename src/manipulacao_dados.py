import json
import os

ARQUIVO_CLIENTES = "data/clientes.json"


def validar_email(email):
    # Verifica se o e-mail contém o caractere '@'
    return "@" in email


def validar_telefone(telefone):
    # Verifica se o telefone contém apenas dígitos e tem 10 ou 11 caracteres
    return telefone.isdigit() and (len(telefone) == 10 or len(telefone) == 11)


def carregar_clientes():
    # Carrega a lista de clientes do arquivo JSON
    # Se o arquivo não existir, retorna uma lista vazia
    if not os.path.exists(ARQUIVO_CLIENTES):
        return []
    with open(ARQUIVO_CLIENTES, 'r') as file:
        return json.load(file)


def salvar_clientes(clientes):
    # Garante que o diretório onde o arquivo será salvo existe
    os.makedirs(os.path.dirname(ARQUIVO_CLIENTES), exist_ok=True)

    # Salva a lista de clientes no arquivo JSON
    with open(ARQUIVO_CLIENTES, 'w') as file:
        json.dump(clientes, file, indent=4)


def add_cliente():
    # Adiciona um novo cliente após validação dos dados inseridos
    clientes = carregar_clientes()
    
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    # Valida o e-mail e o telefone
    while True:
        if not validar_email(email):
            print("\nE-mail inválido.")
            email = input("E-mail: ")
    
        elif not validar_telefone(telefone):
            print("\nTelefone inválido.")
            telefone = input("Telefone: ")
        else:
            break

    # Adiciona o cliente à lista e salva
    cliente = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "telefone": telefone
    }

    clientes.append(cliente)
    salvar_clientes(clientes)
    print("Cliente adicionado com sucesso.")    


def editar_cliente():
    # Edita os dados de um cliente existente
    clientes = carregar_clientes()
    nome = input("Nome do cliente a ser editado: ")

    for cliente in clientes:
        if cliente["nome"] == nome:
            # Solicita novos dados e mantém os valores atuais se nenhum dado for fornecido
            print("Digite os novos dados (deixe em branco para manter o valor atual):")
            novo_nome = input(f"Nome ({cliente['nome']}): ") or cliente['nome']
            nova_idade = input(
                f"Idade ({cliente['idade']}): ") or cliente['idade']
            novo_email = input(
                f"E-mail ({cliente['email']}): ") or cliente['email']
            novo_telefone = input(
                f"Telefone ({cliente['telefone']}): ") or cliente['telefone']

            # Valida os novos dados se fornecidos
            if novo_email and not validar_email(novo_email):
                print("E-mail inválido.")
                return
            if novo_telefone and not validar_telefone(novo_telefone):
                print("Telefone inválido.")
                return

            # Atualiza o cliente e salva
            cliente.update({
                "nome": novo_nome,
                "idade": nova_idade,
                "email": novo_email,
                "telefone": novo_telefone
            })

            salvar_clientes(clientes)
            print("Cliente editado com sucesso.")
            return

    print("Cliente não encontrado.")


def listar_clientes():
    # Lista todos os clientes cadastrados
    clientes = carregar_clientes()
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}, E-mail: {cliente['email']}, Telefone: {cliente['telefone']}")
        print("-" * 100)
        print()

def excluir_cliente():
    # Remove um cliente da lista
    clientes = carregar_clientes()
    nome = input("Nome do cliente a ser excluído: ")

    for cliente in clientes:
        if cliente["nome"] == nome:
            clientes.remove(cliente)
            salvar_clientes(clientes)
            print("Cliente excluído com sucesso.")
            return

    print("Cliente não encontrado.")


def gerar_relatorio_clientes_cadastrados():
    # Gera um relatório de todos os clientes e salva em um arquivo de texto
    clientes = carregar_clientes()
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    relatorio = "Relatório de Clientes Cadastrados\n"
    relatorio += "=" * 30 + "\n"
    for cliente in clientes:
        relatorio += f"Nome: {cliente['nome']}\nIdade: {cliente['idade']}\nE-mail: {cliente['email']}\nTelefone: {cliente['telefone']}\n"
        relatorio += "-" * 30 + "\n"

    with open("relatorio_clientes.txt", 'w') as file:
        file.write(relatorio)

    print("Relatório gerado com sucesso: relatorio_clientes.txt")
