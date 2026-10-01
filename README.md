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

## 📊 Progresso do Projeto

### Dia 3 — Coleta e consolidação dos dados

Foi realizada a coleta dos dados históricos de reclamações de instituições
financeiras disponibilizados pelo Banco Central do Brasil.

Principais etapas:

- Consulta dos períodos disponíveis na API do Banco Central;
- Seleção de dados trimestrais de Bancos e Financeiras a partir de 2017;
- Coleta automática dos arquivos de reclamações;
- Padronização das diferentes estruturas encontradas nos arquivos históricos;
- Consolidação dos dados em uma única base para análise.

A base consolidada contém informações como:

- Ano e trimestre;
- Instituição financeira;
- Reclamações procedentes;
- Total de reclamações;
- Total de clientes.

---

### Dia 4 — Análise exploratória

Com a base histórica consolidada, foi realizada uma análise exploratória
das reclamações entre 2017 e 2026.

Foram analisados:

- Evolução do total de reclamações por ano;
- Instituições com maior volume de reclamações em 2025;
- Instituições com maior número de reclamações procedentes em 2025;
- Evolução histórica das principais instituições;
- Taxa de reclamações por 100 mil clientes.

A normalização pelo número de clientes permitiu comparar instituições
de diferentes tamanhos de forma mais adequada.

### 🔎 Principais insights

- O volume total de reclamações apresentou forte crescimento em 2024 e 2025;
- Bradesco apresentou o maior número absoluto de reclamações procedentes em 2025;
- Agibank apresentou destaque quando as reclamações foram normalizadas pelo número de clientes;
- O crescimento observado em 2024 e 2025 será investigado nas próximas etapas do projeto;
- Os dados de 2026 representam um período ainda incompleto e não devem ser comparados diretamente com anos completos.

### Dia 5 — Investigação do aumento das reclamações ✅

* Análise da evolução anual das reclamações procedentes
* Identificação de um crescimento de 132,06% nas reclamações em 2024
* Comparação entre o crescimento das reclamações e da base de clientes
* Identificação das instituições que mais contribuíram para o aumento
* Cálculo da taxa de reclamações por 100 mil clientes
* Identificação do Agibank como destaque proporcional entre as instituições analisadas

#### 🔎 Principais achados

Em 2024, as reclamações procedentes cresceram 132,06%, maior aumento anual observado no período analisado.

O crescimento da base de clientes, isoladamente, não foi suficiente para explicar esse movimento. Em diversas instituições, as reclamações cresceram muito acima da variação da quantidade de clientes.

Em 2024, Itaú e Caixa apresentaram os maiores aumentos absolutos de reclamações entre as instituições analisadas. Em 2025, Bradesco e PicPay apresentaram os maiores aumentos.

Ao normalizar os resultados pela base de clientes, o Agibank apresentou a maior taxa entre as instituições analisadas, passando de 203,24 reclamações procedentes por 100 mil clientes em 2024 para 248,35 em 2025.

#### ⚠️ Limitação da análise

A base consolidada utilizada nesta etapa não contém o motivo detalhado das reclamações. Por isso, os resultados não permitem determinar se o aumento está relacionado a atendimento, produtos, fraudes, cobranças, canais digitais ou outros fatores.

Uma versão futura do projeto poderá incorporar essas informações para aprofundar a investigação.

