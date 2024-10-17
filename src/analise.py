import pandas as pd

# Importação da base de dados e tratamento básico

df = pd.read_csv('../data/vendas.csv')
df.fillna(0, inplace=True)

# Relação entre gênero e produto comprado

produto_genero = df.groupby(["Gender", "Product Type"]).size().unstack()
produto_genero.to_csv('../data/produto_por_genero.csv')

# Análise de distribuição de clientes por faixa etária

bins = [18, 24, 34, 44, 54, 64, 100] 
labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

faixa_etaria_compras = df['Age Group'].value_counts().sort_index()
faixa_etaria_compras.to_csv('../data/cliente_por_idade.csv')

# Relação entre classificação e quantidade de vendas

classificacao_vendas = df.groupby("Rating")["Quantity"].sum()
classificacao_vendas.to_csv('../data/vendas_por_classificacao.csv')

# Análise de compras por mês

df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
df['Month'] = df['Purchase Date'].dt.month

compras_por_mes = df.groupby('Month')['Quantity'].sum()
compras_por_mes.to_csv('../data/compras_por_mes.csv')

# Análise de métodos de pagamento mais utilizados

metodo_pagamento_quantidade = df.groupby('Payment Method')['Quantity'].sum()
metodo_pagamento_quantidade.to_csv('../data/metodo_pagamento_quantidade.csv')

# Análise de cancelamentos por produto

df_cancelados = df[df['Order Status'] == 'Cancelled']
cancelamentos_por_produto = df_cancelados.groupby('Product Type').size()
cancelamentos_por_produto.to_csv('../data/cancelamentos_por_produto.csv')