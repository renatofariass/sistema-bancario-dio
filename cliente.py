import sqlite3
from conta_bancaria import ContaBancaria
class Cliente:
    def __init__(self, nome, telefone, email, cpf, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf

    @staticmethod
    def conectar():
        return sqlite3.connect("sistema-bancario.db")

    def salvar(self):
        if not all([self.nome, self.telefone, self.email, self.cpf]):
            print("\nErro: Todos os campos (nome, telefone, email, CPF) devem ser preenchidos.\n")
            return None
        
        conexao = Cliente.conectar()
        cursor = conexao.cursor()
        cursor.execute('SELECT id FROM Cliente WHERE cpf=?', (self.cpf,))
        
        resultado = cursor.fetchone()
        if resultado:
            print("\nErro: CPF já cadastrado.\n")
            conexao.close()
            return None
        
        cursor.execute('''
            INSERT INTO Cliente (nome, telefone, email, cpf)
            VALUES (?, ?, ?, ?)
        ''', (self.nome, self.telefone, self.email, self.cpf))
        conexao.commit()
        self.id = cursor.lastrowid
        conexao.close()

        conta = ContaBancaria(cliente_id=self.id)
        return conta.criar_conta()
    
    @staticmethod
    def buscar_por_cpf(cpf):
        conexao = Cliente.conectar()
        cursor = conexao.cursor()
        cursor.execute('SELECT nome, telefone, email, cpf, id FROM Cliente WHERE cpf=?', (cpf,))
        resultado_cliente = cursor.fetchone()
        
        if(resultado_cliente):
            cursor.execute('SELECT * FROM ContaBancaria WHERE cliente_id=?', (resultado_cliente[4],))
            resultado_conta = cursor.fetchone()
            conexao.close()
            
            if resultado_conta:
                cliente = Cliente(resultado_cliente[0], resultado_cliente[1], resultado_cliente[2], 
                                  resultado_cliente[3], resultado_cliente[4])
                conta = ContaBancaria(resultado_conta[0], resultado_conta[1], resultado_conta[2], resultado_conta[3], resultado_conta[4])
                return cliente, conta
            
            return None
