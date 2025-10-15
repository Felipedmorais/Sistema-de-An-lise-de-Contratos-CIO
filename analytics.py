import pandas as pd
import matplotlib.pyplot as plt
from database import conectar

def gerar_relatorio():
    conn = conectar()
    df = pd.read_sql_query("SELECT * FROM funcionarios", conn)
    conn.close()

    if df.empty:
        print("⚠️ Nenhum dado encontrado.")
        return

    df["data_contrato"] = pd.to_datetime(df["data_contrato"])
    df["data_demissao"] = pd.to_datetime(df["data_demissao"], errors="coerce")

    # Estatísticas básicas
    total = len(df)
    ativos = len(df[df["status"] == "Ativo"])
    demitidos = len(df[df["status"] == "Demitido"])

    print(f"\n📊 Relatório Geral")
    print(f"Total de funcionários: {total}")
    print(f"Ativos: {ativos}")
    print(f"Demitidos: {demitidos}")

    # Tempo médio de contrato
    df["tempo_contrato"] = (df["data_demissao"].fillna(pd.Timestamp.now()) - df["data_contrato"]).dt.days
    media_tempo = df["tempo_contrato"].mean()
    print(f"Média de tempo de contrato: {media_tempo:.1f} dias")

    # Gráfico de contratações por mês
    df["mes_contrato"] = df["data_contrato"].dt.to_period("M")
    df_contratos = df.groupby("mes_contrato").size()

    df_contratos.plot(kind="bar", title="Contratações por Mês", figsize=(8,4))
    plt.xlabel("Mês")
    plt.ylabel("Número de Contratações")
    plt.tight_layout()
    plt.show()
    