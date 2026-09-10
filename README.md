# churn-bancario-brasil
Análise de churn e retenção de clientes no setor bancário brasileiro utilizando Python, SQL e Power BI.


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


## 🎯 Perguntas de Negócio

Este projeto busca responder às seguintes perguntas:

### Churn e retenção
1. Qual é a taxa de churn da base de clientes?
2. Como a taxa de churn evolui ao longo do tempo?
3. Quais perfis de clientes apresentam maior taxa de churn?
4. Há diferença de churn de acordo com tempo de relacionamento com o banco?

### Comportamento do cliente
5. Clientes que reduzem sua movimentação financeira apresentam maior probabilidade de churn?
6. Existe redução do saldo ou do número de transações nos meses anteriores ao cancelamento?
7. A quantidade de produtos contratados influencia a permanência do cliente?
8. Quais comportamentos aparecem com maior frequência antes do churn?

### Relacionamento e atendimento
9. Clientes que registram reclamações apresentam maior taxa de churn?
10. Existe relação entre frequência de reclamações e cancelamento?
11. É possível identificar sinais de deterioração do relacionamento antes do encerramento da conta?

### Risco de churn
12. Quais variáveis apresentam maior associação com o churn?
13. É possível criar indicadores para identificar clientes com maior risco de abandono?
14. Quais clientes deveriam ser priorizados em uma estratégia de retenção?

### Mercado bancário brasileiro
15. Como os indicadores de reclamações evoluíram nas instituições financeiras brasileiras?
16. Existem diferenças relevantes nos indicadores entre instituições ou períodos?
17. Como os dados públicos do Banco Central podem complementar a análise de relacionamento e retenção?
