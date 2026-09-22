import requests
import pandas as pd

# Endpoint do Ranking de Reclamações do Banco Central
url_ranking = "https://www3.bcb.gov.br/rdrweb/rest/ext/ranking"

# Faz a requisição
response_ranking = requests.get(url_ranking)

# Verifica se a requisição funcionou
if response_ranking.status_code == 200:
    print("Conexão realizada com sucesso.")
else:
    print("Erro na requisição:", response_ranking.status_code)

# Converte a resposta JSON para Python
dados_ranking = response_ranking.json()

# Acessa os anos disponíveis
anos = dados_ranking["anos"]

# Lista que armazenará os períodos disponíveis
periodos_disponiveis = []

# Percorre a estrutura da API
for ano in anos:
    for periodicidade in ano["periodicidades"]:
        for periodo in periodicidade["periodos"]:
            for tipo in periodo["tipos"]:

                periodos_disponiveis.append({
                    "ano": ano["ano"],
                    "periodicidade": periodicidade["periodicidade"],
                    "periodo": periodo["periodo"],
                    "tipo": tipo["tipo"]
                })

# Transforma a lista em DataFrame
df_periodos = pd.DataFrame(periodos_disponiveis)

# Exibe informações básicas
print("\nPrimeiros registros:")
print(df_periodos.head())

print("\nDimensão da base:")
print(df_periodos.shape)

print("\nAnos disponíveis:")
print(df_periodos["ano"].unique())

# Salva os dados coletados
df_periodos.to_csv(
    "data/periodos_ranking.csv",
    index=False,
    encoding="utf-8"
)

print("\nArquivo salvo em data/periodos_ranking.csv")