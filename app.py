import sqlite3
from banco_de_dados import criar_tabelas
from cliente import Cliente
from conta_bancaria import ContaBancaria

criar_tabelas()

def menu():
    print(' Sistema Bancário '.center(30, "-"))
    print('1. Criar Conta Bancária')
    print('2. Consultar Cliente')
    print('3. Consultar Conta Bancária')
    print('4. Depositar em Conta')
    print('5. Sacar de Conta')
    print('6. Ver Extrato')
    print('7. Fazer Transferência')
    print('8. Sair')

def adicionar_conta():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cpf = input("CPF: ")

    cliente_conta = Cliente(nome, telefone, email, cpf)
    conta = cliente_conta.salvar()
    if conta:
        print('\nSua conta foi criada com sucesso e já está disponível para uso!\n')
        print(' dados da conta '.center(30, "-"))
        print(f'Número da conta: {conta.numero}')
        print(f'Saldo: {conta.saldo:.2f}\n')
        
def consultar_cliente():
    cliente_cpf = input("CPF do Cliente: ")
    resultado = Cliente.buscar_por_cpf(cliente_cpf)
    if not resultado:
        print("\nCliente não encontrado.\n")
        return
        
    cliente, conta = resultado
    print('\n' + ' Dados do cliente '.center(30, "-"))
    print(f"Cliente: {cliente.nome}")
    print(f"Número da conta: {conta.numero}")
    print(f"Email: {cliente.email}")
    print(f"Telefone: {cliente.telefone}\n")
        
def consultar_conta():
    numero = input("Número da Conta: ")
    conta = ContaBancaria.carregar_conta(numero)
    if not conta:
        print("\nConta não encontrada.\n")
        return
    
    print('\n' + ' Dados da conta '.center(30, "-"))
    print(f"Número da Conta: {conta.numero}")
    print(f"Saldo: R${conta.saldo:.2f}\n")

def depositar_em_conta():
    numero = input("Número da Conta: ")
    conta = ContaBancaria.carregar_conta(numero)
    if not conta:
        print("\nConta não encontrada.\n")
        return
    
    valor = float(input("Valor do Depósito: "))
    
    resultado_operacao = conta.depositar(valor)
    if resultado_operacao is False:
        return
    
    print(f"\nDepósito realizado com sucesso.\n")
    print(' Dados da conta '.center(30, "-"))
    print(f"Número da Conta: {conta.numero}")
    valor_anterior = conta.saldo - valor
    print(f"Saldo Anterior: R${valor_anterior:.2f}")
    print(f"Saldo Atual: R${conta.saldo:.2f}\n")


def sacar_de_conta():
    numero = input("Número da Conta: ")
    conta = ContaBancaria.carregar_conta(numero)
    if not conta:
        print("\nConta não encontrada.\n")
        return
        
    valor = float(input("Valor do Saque: "))
    
    resultado_operacao = conta.sacar(valor)
    if resultado_operacao is False:
        return
    
    valor_anterior = conta.saldo + valor
    print(f"\nSaque realizado com sucesso.\n")
    print(' Dados da conta '.center(30, "-"))
    print(f"Número da Conta: {conta.numero}")
    print(f'Saldo Anterior: R${valor_anterior:.2f}')
    print(f"Saldo Atual: R${conta.saldo:.2f}\n")        

def ver_extrato():
    numero = input("Número da Conta: ")
    conta = ContaBancaria.carregar_conta(numero)
    if not conta:
        print("\nConta não encontrada.\n")
        return
        
    conta.ver_extrato()

def transferir_fundos():
    numero_origem = input("Número da Conta de Origem: ")
    conta_origem = ContaBancaria.carregar_conta(numero_origem)
    if not conta_origem:
        print('\nconta não encontrada.\n')
        return
    
    numero_destino = input("Número da Conta de Destino: ")
    valor = float(input("Valor da Transferência: "))
        
    conta_origem.fazer_transferencia(numero_destino, valor)
    
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        print()
        if opcao == '1':
            adicionar_conta()
        elif opcao == '2':
            consultar_cliente()
        elif opcao == '3':
            consultar_conta()
        elif opcao == '4':
            depositar_em_conta()
        elif opcao == '5':
            sacar_de_conta()
        elif opcao == '6':
            ver_extrato()
        elif opcao == '7':
            transferir_fundos()
        elif opcao == '8':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
