🧠 Sistema de Análise de Contratos – CIO

Este projeto é um sistema simples de gerenciamento e análise de funcionários, desenvolvido em Python com SQLite, Pandas e Matplotlib.
Ele permite cadastrar, listar, demitir funcionários e gerar relatórios analíticos com base nos dados registrados.

⚙️ Funcionalidades

📋 Cadastro de funcionários com nome, cargo e data automática de contratação.

🔍 Listagem completa dos funcionários registrados.

🚪 Registro de demissões, alterando o status e data no banco de dados.

📊 Geração de relatórios analíticos com estatísticas (total, ativos, demitidos, tempo médio de contrato) e gráficos de contratações por mês.

🗂️ Estrutura do Projeto

main.py → interface de menu e controle principal.

models.py → operações CRUD com o banco de dados.

analytics.py → geração de relatórios e gráficos.

database.py → criação e conexão com o banco SQLite.

🧰 Tecnologias Utilizadas

Python 3

SQLite3

Pandas

Matplotlib
