import sqlite3
import random
from datetime import datetime

class ContaBancaria:
    MAX_SAQUES = 3 

    def __init__(self, id=None, numero=None, saldo_inicial=0, cliente_id=None, saques=0):
        self.id = id
        self.numero = numero if numero is not None else self.gerar_numero_conta()
        self.cliente_id = cliente_id
        self.saldo = saldo_inicial
        self.saques = saques  

    @staticmethod
    def gerar_numero_conta():
        return random.randint(100000, 999999)

    @staticmethod
    def conectar():
        return sqlite3.connect('sistema-bancario.db')

    def criar_conta(self):
        conexao = ContaBancaria.conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO ContaBancaria (numero, saldo, cliente_id, saques)
            VALUES (?, ?, ?, ?)
        ''', (self.numero, self.saldo, self.cliente_id, self.saques))
        conexao.commit()
        self.id = cursor.lastrowid
        conexao.close()
        
        return ContaBancaria(self.id, self.numero, self.saldo, self.cliente_id, self.saques)
                
    @staticmethod
    def carregar_conta(numero):
        conexao = ContaBancaria.conectar()
        cursor = conexao.cursor()
        cursor.execute('SELECT id, numero, saldo, cliente_id, saques FROM ContaBancaria WHERE numero=?', (numero,))
        resultado = cursor.fetchone()
        conexao.close()
        
        if resultado:
            return ContaBancaria(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
        
        return None
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.adicionar_extrato("Depósito", valor)
            self.atualizar_saldo()
            return True
        else:
            print('\nValor de depósito inválido.\n')
            return False
            
    def sacar(self, valor):
        if self.saques >= ContaBancaria.MAX_SAQUES:
            print('\nLimite de saques atingido.\n')
            return False
        
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.saques += 1
            self.adicionar_extrato("Saque", -valor)
            self.atualizar_saldo()
            return True
        else: 
            print('\nSaldo insuficiente ou valor de saque inválido.\n')
            return False
            
    def atualizar_saldo(self):
        conexao = ContaBancaria.conectar()
        cursor = conexao.cursor()
        cursor.execute('UPDATE ContaBancaria SET saldo=?, saques=? WHERE numero=?', (self.saldo, self.saques, self.numero))
        conexao.commit()
        conexao.close()
        
    def adicionar_extrato(self, descricao, valor):
        conexao = ContaBancaria.conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO Extrato (conta_numero, data, descricao, valor)
            VALUES (?, ?, ?, ?)
        ''', (self.numero, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), descricao, valor))
        conexao.commit()
        conexao.close()
        
    def ver_extrato(self):
        conexao = ContaBancaria.conectar()
        cursor = conexao.cursor()
        cursor.execute('SELECT data, descricao, valor FROM Extrato WHERE conta_numero=? ORDER BY data DESC', (self.numero,))
        extrato = cursor.fetchall()
        conexao.close()
        
        print()
        print(f' Extrato da conta: {self.numero} '.center(40, "-"))
    
        for movimento in extrato:
            print(f"{movimento[0]} - {movimento[1]}: R${movimento[2]:.2f}")
        print(f"Saldo atual: R${self.saldo:.2f}\n")
        
    def fazer_transferencia(self, numero_destino, valor):
        if valor <= 0:
            print('Valor de transferência inválido.')
            return

        if valor > self.saldo:
            print('Saldo insuficiente para transferência.')
            return

        conta_destino = ContaBancaria.carregar_conta(numero_destino)
        if not conta_destino:
            print('Conta destino não encontrada.')
            return

        self.saldo -= valor
        conta_destino.saldo += valor
        self.adicionar_extrato('Transferência para conta {}'.format(numero_destino), -valor)
        conta_destino.adicionar_extrato('Transferência recebida da conta {}'.format(self.numero), valor)

        self.atualizar_saldo()
        conta_destino.atualizar_saldo()

        print(f'\nTransferência de R${valor:.2f} para a conta {numero_destino} realizada com sucesso.\n')