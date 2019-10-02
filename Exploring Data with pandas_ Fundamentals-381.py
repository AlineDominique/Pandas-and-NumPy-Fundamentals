## 1. Introduction to the Data ##

#Já lemos o conjunto de dados em um dataframe do pandas e o atribuímos a uma variável chamada f500.
    #1. Use o método Dataframe.head() para selecionar as 10 primeiras linhas do dataframe f500. Atribua o resultado ao f500_head.
f500_head = f500.head(10)
    #2. Use o método Dataframe.info() para visualizar a informação sobre o dataframe.
f500.info()

## 2. Vectorized Operations ##

#1. Subtrair os valores da coluna rank dos valores da coluna previous_rank. Atribua o resultado rank_change.
rank_change = f500["previous_rank"] - f500["rank"]

## 3. Series Data Exploration Methods ##

rank_change =  f500["previous_rank"] - f500["rank"]
#1. Use o método Series.max() para encontrar o valor máximo do rank_change. Atribua o resultado a variavel rank_change_max.
rank_change_max = rank_change.max()
#2. Use o método Series.min() para encontrar o valor máximo do rank_change. Atribua o resultado a variavel rank_change_min.
rank_change_min = rank_change.min()
#3. Depois  execute o seu código,use inspeto de variavel para visualizar cada nova variavel criada.

## 4. Series Describe Method ##

#1. Retorne uma série de estatísticas descritivas para a coluna rank do f500.
    #Selecione a coluna rank. Atribua-o a uma variável chamada rank.
    #Use o método Series.describe () para retornar uma série de estatísticas da coluna rank. Atribua o resultado a rank_desc.
rank = f500["rank"]
rank_desc = rank.describe()
#2. Retorne uma série de estatísticas descritivas para a coluna de previous_rank do f500.
    #Selecione a coluna previous_rank. Atribua-o a uma variável chamada prev_rank.
    #Use o método Series.describe () para retornar uma série de estatísticas da coluna prev_rank. Atribua o resultado a prev_rank_desc.
prev_rank = f500["previous_rank"]
prev_rank_desc = prev_rank.describe()
#3. Depois  execute o seu código,use inspeto de variavel para visualizar cada nova variavel criada.Tente identificar os possíveis problemas com o data antes de ir para proxima tela.

## 5. Method Chaining ##

#1. Use os métodos Series.value_counts() e Series.loc para retornar o número de companias com valor 0 na coluna previous_rank no dataframe f500. Atribua o resultado para zero_previous_rank.
zero_previous_rank = f500["previous_rank"].value_counts().loc[0]
#2. Depois de executar o código, use o inspetor de variavel para visualizar a variavel criada.

## 6. Dataframe Exploration Methods ##

#1. Use o método DataFrame.max() para encontrar o valor máximo apenas das colunas que possui o valor numerico no f500.(talvez seja necessário verificar a documentação).Atribua o resultado a variavel max_f500.
max_f500 = f500.max(numeric_only=True)
#2. Depois  execute o seu código,use inspeto de variavel para visualizar cada nova variavel criada.Tente identificar os possíveis problemas com o data antes de ir para proxima tela.


## 7. Dataframe Describe Method ##

#1. Retorne um quadro de estatísticas descritivas dos dados para todas as colunas numéricas em f500. Atribua o resultado a f500_desc.
f500_desc = f500.describe()
#2. Depois  execute o seu código,use inspeto de variavel para visualizar cada nova variavel criada.Tente identificar os possíveis problemas com o data antes de ir para proxima tela.

## 8. Assignment with pandas ##

#1. A compania Dow Chemical tem um novo CEO. Ataulize o valor da label Dow Chemical na colna ceo com o nome Jim Fitterling no dataframe f500.
f500.loc["Dow Chemical","ceo"] = "Jim Fitterling"
print(f500.loc["Dow Chemical","ceo"] )

## 9. Using Boolean Indexing with pandas Objects ##

#1. Criar um series boolean, motor_bool, eme que compare os valores da coluna industry do dataframe f500 são iguais ao "Motor Vehicles and Parts".
motor_bool = f500["industry"] == "Motor Vehicles and Parts"
#2. Use o boolean motor_bool para anexar a coluna country. Atribua o resultado a motor_countries.
motor_countries = f500.loc[motor_bool,"country"]
#3. Depois execute o código, use o inspetor de variavel para visualizar cada variavel criada.

## 10. Using Boolean Arrays to Assign Values ##

import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
#Use a indexação booleana para atualizar valores na coluna previous_rank do dataframe f500:
    #Agora deve haver um valor de np.nan em que anteriormente havia um valor de 0.
    #Depende de você atribuir primeiro a série booleana à sua própria variável ou concluir a operação em uma linha.
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
#Crie uma nova série de pandas, prev_rank_after, usando a mesma sintaxe para criar a série prev_rank_before.
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()
#Depois de executar seu código, use o inspetor de variáveis para comparar prev_rank_before e prev_rank_after.
#Os valores que eram 0 na coluna previous_rank foram alterados por nan.

## 11. Creating New Columns ##

#1. Adicione uma nova coluna denominada rank_change ao dataframe f500 subtraindo os valores da coluna rank dos valores da coluna previous_rank.
f500["rank_change"] = f500["previous_rank"] - f500["rank"]
#2. Use o método Series.describe () para retornar uma série de estatísticas descritivas para a coluna rank_change. Atribua o resultado a rank_change_desc.
rank_change_desc = f500["rank_change"].describe()
#3. Depois de executar seu código, use o inspetor de variáveis para visualizar cada uma das novas variáveis que você criou. Verifique se o valor mínimo da coluna rank_change agora é maior que -500.


## 12. Challenge: Top Performers by Country ##

#1. Crie uma série, industry_usa, contendo contagens dos dois valores mais comuns na coluna setor para empresas com sede nos EUA.
industry_usa = f500["industry"][f500["country"] == "USA"].value_counts().head(2)
#2. Crie uma série, setor_china, contendo contagens dos três valores mais comuns na coluna setor para empresas com sede na China.
sector_china = f500["sector"][f500["country"] == "China"].value_counts().head(3)