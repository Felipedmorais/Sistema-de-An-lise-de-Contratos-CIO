import sqlite3

# Função para conectar ao banco de dados
def conectar():
    """Cria e retorna uma conexão com o banco de dados."""
    return sqlite3.connect("empresa.db")

# Função para criar a tabela, se ainda não existir
def criar_tabelas():
    """Cria a tabela 'funcionarios' caso não exista."""
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            data_contrato TEXT NOT NULL,
            data_demissao TEXT,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
