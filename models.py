from database import conectar


def adicionar_funcionario(nome, cargo, data_contrato):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO funcionarios (nome, cargo, data_contrato, status)
        VALUES (?, ?, ?, ?)
    """, (nome, cargo, data_contrato, "Ativo"))
    conn.commit()
    conn.close()

def demitir_funcionario(id_funcionario, data_demissao):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        UPDATE funcionarios
        SET data_demissao = ?, status = ?
        WHERE id = ?
    """, (data_demissao, "Demitido", id_funcionario))
    conn.commit()
    conn.close()

def listar_funcionarios():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM funcionarios")
    dados = cur.fetchall()
    conn.close()
    return dados
    