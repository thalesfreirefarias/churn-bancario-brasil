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


---------------

## 📅 Progresso do Projeto

### Dia 1 — Mapeamento da API do Banco Central ✅

- Exploração da API de Ranking de Reclamações do BCB
- Identificação dos anos e períodos disponíveis
- Estruturação dos períodos em DataFrame
- Análise das periodicidades disponíveis
- Definição do recorte do projeto

### Dia 2 — Coleta histórica de reclamações ✅

- Definição do período de análise a partir de 2017
- Seleção de bancos e financeiras
- Automatização da coleta trimestral via API
- Coleta de 37 períodos disponíveis entre 2017 e 2026
- Consolidação de 5.060 registros em um único DataFrame
- Identificação de ausência do 2º trimestre de 2022 na listagem de períodos da API
- Identificação de mudanças no schema dos arquivos ao longo dos anos
- Preservação dos dados brutos para posterior tratamento e padronização

### Próxima etapa — Tratamento dos dados 🔄

- Padronizar nomes das colunas
- Corrigir problemas de encoding
- Harmonizar mudanças de schema entre os períodos
- Selecionar variáveis relevantes para análise
- Criar a camada de dados processados

