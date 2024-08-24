import sqlite3
from conta_bancaria import ContaBancaria
class Cliente:
    def __init__(self, nome, telefone, email, cpf, id=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.id = id

    @staticmethod
    def conectar():
        return sqlite3.connect("sistema-bancario.db")

    def salvar(self):
        conexao = Cliente.conectar()
        cursor = conexao.cursor()
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
        cursor.execute('SELECT * FROM Cliente WHERE cpf=?', (cpf,))
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return Cliente(resultado[1], resultado[2], resultado[3], resultado[4], resultado[0])
        return None
