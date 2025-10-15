from database import criar_tabelas
from models import adicionar_funcionario, demitir_funcionario, listar_funcionarios
from analytics import gerar_relatorio
from datetime import datetime

def menu():
    print("""
=== Sistema de Análise de Contratos - CIO ===
1. Adicionar funcionário
2. Listar funcionários
3. Registrar demissão
4. Gerar relatório analítico
0. Sair
""")

def main():
    criar_tabelas()
    while True:
        menu()
        op = input("Escolha: ")
        if op == "1":
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            data_contrato = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            adicionar_funcionario(nome, cargo, data_contrato)
            print("✅ Funcionário adicionado.")
        elif op == "2":
            funcionarios = listar_funcionarios()
            print("\n--- Lista de Funcionários ---")
            for f in funcionarios:
                print(f)
        elif op == "3":
            idf = int(input("ID do funcionário: "))
            data_demissao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            demitir_funcionario(idf, data_demissao)
            print("🚪 Funcionário demitido.")
        elif op == "4":
            gerar_relatorio()
        elif op == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()