# Sistema de Cadastro de Clientes

Este é um sistema simples de cadastro de clientes em Python que permite adicionar, editar, listar, excluir e gerar relatórios de clientes. Os dados dos clientes são armazenados em um arquivo JSON para persistência.

## Funcionalidades

- **Adicionar Cliente:** Cadastra um novo cliente com nome, idade, e-mail e telefone.
- **Editar Cliente:** Atualiza os dados de um cliente existente.
- **Listar Clientes:** Exibe todos os clientes cadastrados.
- **Excluir Cliente:** Remove um cliente do sistema.
- **Gerar Relatório:** Gera um relatório com todos os clientes cadastrados e o salva em um arquivo de texto.

## Requisitos

- Python 3.x
- Biblioteca padrão do Python (não são necessárias bibliotecas adicionais)

## Estrutura do Projeto

- `interface_usuario.py`: Contém a função para exibir o menu de opções.
- `manipulacao_dados.py`: Contém funções para manipulação dos dados dos clientes, incluindo validação e armazenamento.
- `main.py`: Arquivo principal que executa o programa e coordena as operações com base na escolha do usuário.

## Como Usar

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/yourusername/sistema-de-cadastro-de-clientes.git
    ```

2. **Navegue até o diretório do projeto:**

    ```bash
    cd sistema-de-cadastro-de-clientes/src
    ```

3. **Execute o programa:**

    ```bash
    python main.py
    ```

4. **Siga as instruções no menu para adicionar, editar, listar, excluir clientes e gerar relatórios.**

## Exemplos de Uso

### Adicionar Cliente

1. Escolha a opção `1 - Adicionar cliente`.
2. Insira as informações solicitadas: nome, idade, e-mail e telefone.
3. O cliente será adicionado e salvo no arquivo JSON.

### Editar Cliente

1. Escolha a opção `2 - Editar cliente`.
2. Informe o nome do cliente a ser editado.
3. Digite os novos dados (ou deixe em branco para manter os valores atuais).

### Listar Clientes

1. Escolha a opção `3 - Listar clientes`.
2. O sistema exibirá todos os clientes cadastrados.

### Excluir Cliente

1. Escolha a opção `4 - Excluir cliente`.
2. Informe o nome do cliente a ser excluído.
3. O cliente será removido da lista e do arquivo JSON.

### Gerar Relatório

1. Escolha a opção `5 - Gerar relatório de clientes cadastrados`.
2. Um arquivo `relatorio_clientes.txt` será criado com os dados dos clientes.

## Notas

- O diretório `data` é criado automaticamente se não existir.
- O arquivo JSON é salvo como `data/clientes.json`.
- O relatório é salvo como `relatorio_clientes.txt` no diretório atual.

## Contribuição

Se você quiser contribuir para o projeto, sinta-se à vontade para enviar pull requests ou relatar problemas.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Desenvolvido por [PenhaJV](https://github.com/PenhaJV).
