# Sistema Bancário em Python

Este é um projeto simples de um sistema bancário desenvolvido em Python, utilizando SQLite como banco de dados. O sistema permite a criação de contas bancárias, depósito, saque, consulta de clientes, consulta de contas, visualização de extrato e transferências entre contas.

## ⚙️ Funcionalidades

- **Criar Conta Bancária**: Cria uma nova conta bancária associada a um cliente.
- **Consultar Cliente**: Exibe os dados de um cliente a partir do CPF.
- **Consultar Conta Bancária**: Exibe os dados de uma conta bancária a partir do número da conta.
- **Depositar em Conta**: Permite realizar depósitos em uma conta bancária existente.
- **Sacar de Conta**: Permite realizar saques de uma conta bancária existente.
- **Ver Extrato**: Exibe o extrato de transações de uma conta bancária.
- **Fazer Transferência**: Realiza transferências de fundos entre contas bancárias.

##   📁 Estrutura do Projeto

- **`banco_de_dados.py`**: Script responsável por criar as tabelas no banco de dados SQLite.
- **`cliente.py`**: Contém a classe `Cliente`, responsável por gerenciar as operações relacionadas ao cliente, como salvar e buscar clientes.
- **`conta_bancaria.py`**: Contém a classe `ContaBancaria`, que gerencia operações relacionadas à conta bancária, como criar conta, depositar, sacar, ver extrato e realizar transferências.
- **`app.py`**: Script principal que executa o sistema bancário, proporcionando uma interface de linha de comando para o usuário interagir com o sistema.

## 🛠️ Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/renatofariass/sistema-bancario-python.git
   ```
2. **Abra a pasta do projeto no vscode, ou na IDE de sua preferência e aperte play no arquivo "app.py" ou abra um terminal dentro da pasta e rode:**
    ```
    python app.py
    ```

## 👨🏻‍💻 Autor
Renato Alberto  
https://linkedin.com/in/renatofari4s