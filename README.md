# 📊 Análise de Reclamações no Setor Bancário Brasileiro

Projeto de análise de dados utilizando informações públicas do Banco Central
do Brasil para estudar a evolução das reclamações relacionadas às instituições
financeiras brasileiras.

## 🎯 Objetivo

Analisar os dados públicos do Ranking de Reclamações do Banco Central,
identificando padrões, evolução ao longo do tempo e diferenças entre
instituições financeiras.

## 🛠️ Tecnologias

- Python
- Pandas
- Requests
- Git/GitHub

## 📂 Estrutura do projeto

- `src/` — scripts Python
- `data/` — dados utilizados no projeto
- `notebooks/` — análises exploratórias
- `dashboard/` — visualizações futuras


⚙️ Configuração do ambiente

Este projeto utiliza um ambiente virtual Python (venv) para isolar as dependências e garantir maior organização e reprodutibilidade.

1. Clonar o repositório
git clone https://github.com/thalesfreirefarias/churn-bancario-brasil.git
cd churn-bancario-brasil
2. Criar o ambiente virtual
python3 -m venv .venv
3. Ativar o ambiente virtual

No macOS/Linux:

source .venv/bin/activate

Após a ativação, o terminal deverá apresentar (.venv) no início da linha.

4. Instalar as dependências
pip install -r requirements.txt

As principais bibliotecas utilizadas no projeto incluem Pandas para manipulação e análise de dados e Requests para coleta de dados de fontes externas.

A pasta .venv não é versionada no GitHub. As dependências necessárias para reproduzir o ambiente do projeto são registradas no arquivo requirements.txt.

