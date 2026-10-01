## 📅 Progresso do Projeto

### Dia 1 — Mapeamento da API do Banco Central ✅

Primeiro contato com a API do Ranking de Reclamações do Banco Central para entender a estrutura e definir o recorte da análise.

Principais etapas:

- Exploração da API de Ranking de Reclamações do BCB;
- Identificação dos anos e períodos disponíveis;
- Estruturação dos períodos em DataFrame;
- Análise das periodicidades disponíveis;
- Definição do recorte do projeto.

---

### Dia 2 — Coleta histórica de reclamações ✅

Automatização da coleta dos arquivos históricos disponibilizados pelo Banco Central.

Principais etapas:

- Definição do período de análise a partir de 2017;
- Seleção de Bancos e Financeiras;
- Automatização da coleta trimestral via API;
- Coleta de 37 períodos disponíveis entre 2017 e 2026;
- Consolidação inicial de 5.060 registros;
- Identificação de mudanças na estrutura dos arquivos ao longo dos anos;
- Preservação dos dados brutos para tratamento posterior.

Também foi identificada a ausência do 2º trimestre de 2022 na listagem de períodos retornada pela API.

---

### Dia 3 — Tratamento e consolidação dos dados ✅

Os arquivos históricos apresentam estruturas diferentes dependendo do período analisado.

Nesta etapa foi realizada a preparação necessária para criar uma base única e consistente para análise.

Principais etapas:

- Padronização dos nomes das colunas;
- Tratamento das diferenças de estrutura entre os arquivos históricos;
- Remoção de colunas desnecessárias;
- Seleção das variáveis relevantes;
- Conversão e tratamento dos dados;
- Consolidação dos diferentes períodos em uma única base.

A base final utilizada nas análises contém:

- Ano;
- Trimestre;
- Instituição financeira;
- Reclamações procedentes;
- Total de reclamações;
- Total de clientes.

---

### Dia 4 — Análise exploratória dos dados ✅

Com a base histórica consolidada, foi realizada uma análise exploratória das reclamações entre 2017 e 2026.

Foram analisados:

- Evolução das reclamações ao longo dos anos;
- Instituições com maior volume de reclamações;
- Instituições com maior número de reclamações procedentes;
- Evolução histórica das principais instituições;
- Relação entre reclamações e tamanho da base de clientes.

### 🔎 Principais insights

- O volume de reclamações apresentou forte crescimento em 2024 e 2025;
- Bradesco apresentou o maior número absoluto de reclamações procedentes em 2025;
- Agibank apresentou destaque quando as reclamações foram normalizadas pelo número de clientes;
- Os dados de 2026 representam um período ainda incompleto e, portanto, não devem ser comparados diretamente com anos completos.

O crescimento observado em 2024 e 2025 levou à investigação realizada no Dia 5.

---

### Dia 5 — Investigação do aumento das reclamações ✅

A partir dos resultados da análise exploratória, foi investigado se o forte aumento das reclamações em 2024 e 2025 poderia ser explicado pelo crescimento da base de clientes das instituições.

### 📈 Evolução das reclamações

A análise da variação anual mostrou que:

- **2024:** +132,06%;
- **2025:** +36,84%.

O ano de 2024 apresentou o maior crescimento anual de reclamações procedentes dentro do período analisado.

### 👥 Reclamações x crescimento da base de clientes

Foi comparada a evolução das reclamações com a evolução da base média de clientes das principais instituições.

Os resultados mostraram que o crescimento da base de clientes, isoladamente, não é suficiente para explicar o aumento observado.

Em diversas instituições, as reclamações cresceram muito acima da variação da quantidade de clientes.

No Itaú, por exemplo, em 2024:

- Reclamações procedentes: **+117,89%**;
- Base média de clientes: **-0,61%**.

### 🏦 Instituições que mais contribuíram para o aumento

Em números absolutos, os maiores aumentos entre as instituições analisadas foram:

**2024**

- Itaú: +7.275 reclamações;
- Caixa: +7.239;
- Agibank: +5.258.

**2025**

- Bradesco: +11.925;
- PicPay: +10.131;
- Agibank: +7.305.

A análise também demonstrou a importância de diferenciar crescimento percentual de crescimento absoluto.

### 📊 Reclamações por 100 mil clientes

Para comparar instituições de diferentes tamanhos, foi calculada a quantidade de reclamações procedentes por 100 mil clientes.

O Agibank apresentou a maior taxa entre as instituições analisadas:

- **2024:** 203,24 reclamações por 100 mil clientes;
- **2025:** 248,35 reclamações por 100 mil clientes.

O PicPay também apresentou crescimento relevante:

- **2024:** 2,90;
- **2025:** 18,37 reclamações por 100 mil clientes.

A Caixa permaneceu praticamente estável:

- **2024:** 9,28;
- **2025:** 9,08.

### 💡 Conclusão da investigação

A análise identificou um forte crescimento das reclamações procedentes em 2024, com continuidade do aumento em 2025.

O crescimento da base de clientes não foi suficiente para explicar esse movimento. Em diversas instituições, as reclamações cresceram muito acima da variação da quantidade de clientes.

Além disso, o crescimento permaneceu relevante mesmo após a normalização das reclamações pelo tamanho da base.

### ⚠️ Limitação da análise

A base consolidada utilizada nesta versão do projeto não contém o motivo detalhado das reclamações.

Portanto, os dados analisados não permitem determinar se o crescimento está relacionado a atendimento, produtos, fraudes, cobranças, canais digitais ou outros fatores.

Uma versão futura do projeto poderá incorporar dados detalhados sobre os motivos das reclamações para aprofundar essa investigação.

---

### Próxima etapa — Documentação e apresentação do projeto 🔄

A próxima etapa será dedicada à finalização da primeira versão do projeto:

- Revisão e organização do README;
- Documentação da metodologia;
- Organização dos scripts;
- Apresentação dos principais resultados;
- Documentação das limitações;
- Definição de possíveis evoluções futuras do projeto.
