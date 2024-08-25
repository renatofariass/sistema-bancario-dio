import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema-bancario.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ContaBancaria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL,
            saldo REAL NOT NULL,
            saques INTEGER DEFAULT 0,
            cliente_id INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
                ON DELETE CASCADE
                ON UPDATE NO ACTION
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Extrato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conta_numero TEXT,
            data TEXT NOT NULL,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            FOREIGN KEY (conta_numero) REFERENCES ContaBancaria(numero)
        )
    ''')

    conexao.commit()
    conexao.close()