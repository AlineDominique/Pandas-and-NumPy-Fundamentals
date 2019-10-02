## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
# ler o dataset com dataframe pandas.
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
# substituição dos valores 0 da coluna previous_rank para NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

#Nós já lemos o dataset através do dataframe pandas e atribui a variavel de nome f500. Nós também mudamos todos os valores 0 na coluna previous_rank para NaN, como foi feito na missão anterior.
    #1. Selecione as colunas rank,revenues e revenue_change no f500. Usando o método Dataframe.head() para selecionar as 5 primeiras linhas. Atribua o restultado para f500_selection.
f500_selection = f500[["rank","revenues","revenue_change"]].head(5)
    #2. Use o inspetor de variavel para visualizar o f500_selection.Compare o resultado das 5 primeiras linhas.
    #3. Dê uma olhada na documentação da função pandas.read_csv para tentar entender os resultados. Se não tiver problema para entender, não se preocupe!Nós iremos explicar o resultado na próxima tela.

## 2. Reading CSV files with pandas ##

#1. Use a função de pandas.read_csv() par ler o arquivo f500.csv como dataframe. Atribua a variavel de nome f500.
    #Não use o parametros index_col.
f500 = pd.read_csv("f500.csv")
#2. Use o código abaixo para inserir os valores NaN na coluna previous_rank:
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

#1. Selecione apenas as quize linhas do dataframe f500. Atribua o resultado a variavel fifth_row.
fifth_row = f500.iloc[4]
#2. Selecione o primeiro valor da linha da coluna company. Atribua o resultado a variavel company_value.
company_value = f500.iloc[0,0]

## 4. Using iloc to select by integer position continued ##

#1. Selecione as três primeiras linhas do dataframe f500. Atribua o resultado a variavel first_three_rows.
first_three_rows = f500[:3]
#2. Selecione a primera e setima linha das quatro primeiras columns do f500.Atribua o resultado a variavel first_seventh_row_slice.
first_seventh_row_slice = f500.iloc[[0,6],:5]
#3. Depois execute o código, use o inspsetor de variavel pra examinar cada objeto criado.

## 5. Using pandas methods to create boolean masks ##

#1. Use o método Series.isnull para selecionar todas linhas do dataframe f500 que tenha valores null na coluna previous_rank. Selecione apenas as colunas company, rank e previous_rank. Atribua o resultado ao null_previous_rank.
null_previous_rank = f500[f500["previous_rank"].isnull()][["company","rank","previous_rank"]]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]
#1. Atribua as cinco linhas do dataframe null_previous_rank à variavel top5_null_prev_rank escolhendo o método correto dentre loc [] ou iloc [].
top5_null_prev_rank = null_previous_rank.iloc[:5]

## 7. Pandas Index Alignment ##

#1. Use o método o Series.notnull() para selecionar todas as linhas do f500 que não possui valores non-null da coluna previous_rank. Atribua o resultado a variavel previous_rank.
previously_ranked = f500[f500["previous_rank"].notnull()]
#2. Do dataframe previously_ranked, subtrai a coluna rank da coluna previous_rank. Atribua o resltado ao rank_change.
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
#3. Atribua os valores do rank_change a uma nova coluna no dataframe f500, rank_change.
f500["rank_change"] = rank_change
#4. Assim que executar o seu código, use o inspetor de variavel para verificar o dataframe e observe como a nova coluna se alinha com os dados existente.


## 8. Using Boolean Operators ##

#1. Selecione todas companias com revenues maior que 100 billion e profits negativos do dataframe f500. O resultado teve incluir todas colunas.
    #Selecione as companias com revenues maior qe 100 billion. Atribua o resultado a variavel large_revenue.
large_revenue = f500["revenues"] > 100000
    #Selecione as companias com profits menor que 0. Atribua o resultado a variavel negative_profits.
negative_profits = f500["profits"] < 0    
    #Combine large_revenue e negative_profits.Atribua o resultado a variavel combined.
combined = large_revenue & negative_profits
    #Use o combined como filtro no f500. Atribua o resultado a variavel big_rev_neg_profit.
big_rev_neg_profit = f500[combined]

## 9. Using Boolean Operators Continued ##

#1. Selecione todas as companias que tem sede no Brasil e na Venezuela. Atribua o resultado a variavel brazil_venezuela.
filter_brazil_venezuela = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")
brazil_venezuela = f500[filter_brazil_venezuela]
#2. Selecione as cinco primeiras companias do setor de Tecnologia que não tem sede no USA do dataframe f500. Atribua o resultado a variavel tech_outside_usa.
filter_tech_outside_usa = (f500["sector"] == "Technology") & ~(f500["country"] == "USA")
tech_outside_usa = f500[filter_tech_outside_usa].head()

## 10. Sorting Values ##

#1. Encontre a compania com sede no Japão com maior número de funcionários.
    #Selecione apenas as linhas que contenham o nome do país igual a Japan(Japão).
filter_japan = f500[f500["country"] == "Japan"]
    #Use o metodo Dataframe.sort_values() para ordenar as linhas da coluna employees de forma decrescente.
sort_values = filter_japan.sort_values("employees",ascending=False)   
    #Use o metodo Dataframe.iloc[] para selecionar a primeira linha do dataframe ordenado.
sort_values.iloc[0]
    #Extrai o nome da compania do index label company da primeira linha. Atribua o resultado a variavel top_japanese_employer.
top_japanese_employer = sort_values.iloc[0]["company"]
#2. Depois e executar o código, use o inspetor de variavel para visualizar o maior empregador do Japão.

## 11. Using Loops with pandas ##

#Neste  exercicio, nós iremos criar um dicionário com os maiores empregadores de cada país.
    #1. Crie um dicionário vazio com o nome de top_employer_by_country onde armazenaremos os resultados deste exercicio.
top_employer_by_country = {}
    #2. Use o método Series.unique() para criar um array com valores unicos da coluna country.
countries = f500["country"].unique()
    #3. Use um for loop para percorrer o array countries. A cada iterção:
        #Selecione apenas as linhas que tenha o nome dos paises igual para a iteração atual.
        #Use o metodo Dataframe.sort_values() para ordernar as linhas pela coluna employees de forma decrescente.
        #Selecione a primeira linha do dataframe ordernado.
        #Extrai o nome da compania do index label company da primeira linha.
        #Atribua os resultados ao dicionário top_employer_by_country, usando o paises o nome dos paises que são chaves, e o nome da compania com o valor.
for c in countries:
    selected_rows = f500[f500["country"] == c]
    sorted_rows = selected_rows.sort_values("employees", ascending=False)
    top_employer = sorted_rows.iloc[0]
    employer_name = top_employer["company"]
    top_employer_by_country[c] = employer_name
#4. Depois de executar o código, use o inspetor de variavel para visualizar os maiores empregadores de cada paises.
print(top_employer_by_country)

## 12. Challenge: Calculating Return on Assets by Country ##

#1. Crie um nova coluna roa no dataframe f500, contendo a métrica de ativos para cada empresa.
f500["roa"] = f500["profits"]/f500["assets"]
#2. Agregue os dados pela coluna setor e crie um dicionário top_roa_by_sector, com:
    #Chaves do dicionário é o nome do setor.
    #O valor do dicionário é com o nome da compania e maior valor do ROA do sector.
top_roa_by_sector = {}
for sector in f500["sector"].unique():
    is_sector = f500["sector"] == sector
    sector_companies = f500.loc[is_sector]
    top_company = sector_companies.sort_values("roa",ascending=False).iloc[0]
    company_name = top_company["company"]
    top_roa_by_sector[sector] = company_name

                               
    