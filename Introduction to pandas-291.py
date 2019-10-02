## 2. Introduction to the Data ##

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

#1. Use a função type() do Python na variavel f500 e atribuir a variavel f500_type.
f500_type = type(f500)
#2. Use o atributo DataFrame.shape e atribua a forma do f500 a variavel f500_shape.
f500_shape = f500.shape
#3. Depois execute o  seu código, e use inspetor de variavel para visualizar o conteudo das variaveis: f500,f500_type e f500_shape.
#R: f500 mostra o DataFrame, f500_type mostra o tipo da variavel(pandas.core.frame.DataFrame) e f500_shape mostra a quantidade de colunas e da linhas.

## 3. Introducing DataFrames ##

#A variavel f500 criada na tela anterior está disponível para ser usada aqui.
#1. Use o método head() para selecionar as 6 primeiras linhas dataset. Atribua o resultado a f500_head.
f500_head = f500.head(6)
#2. Use o método tail() para selecionar as 8 ultimas linhas do dataset.Atribua o resultado a f500_tail.
f500_tail = f500.tail(8)
#3. Depois de excutar o código, use o inspetor de variavel para visualizar as informações do dataframe.


## 5. Selecting a Column From a DataFrame by Label ##

#1. Selecione a coluna industry. Atribua o resultado da variavel o nome industries.
industries = f500.loc[:,"industry"]
#2. Use a função type() do Python para descobrir o tipo do industries e atribua a variavel industries_type
industries_type = type(industries)
#3. Depois executar o código, use o inspetor de variavel para verificar a variavel.

## 7. Selecting Columns From a DataFrame by Label Continued ##

#1. Selecione a coluna country. Atribua o resultado a variavel de nome countries.
countries = f500["country"]
#2. Na seguiente ordem, selecione as colunas revenues e years_on_global_500_list. Atribua o resultado a variavel de nome revenues_years.
revenues_years = f500[["revenues","years_on_global_500_list"]]
#3. Na seguiente ordem, selecione todas colunas ceo e inclua o sector. Atribua o resultado a variavel de nome ceo_to_sector.
ceo_to_sector = f500.loc[:,"ceo":"sector"]
#Depois execute o seu código, use o inspetor de variavel para visualizar o conteudo das variaveis.

## 8. Selecting Rows From a DataFrame by Label ##

#Selecionando dados de f500:
    #1. Criar um nova variavel toyota, com:
        #Com apenas a linha do index Toyota Motor.
        #Todas colunas.
toyota = f500.loc['Toyota Motor']
    #2. Criar uma nov variavel,drink_companies, com:
        #Com as linhas do index Anheuser-Busch InBev, Coca-Cola, e Heineken Holding, nesta ordem.
        #Todas colunas.
drink_companies = f500.loc[["Anheuser-Busch InBev","Coca-Cola","Heineken Holding"]]
    #3. Criar um nova variavel, middle_companies com:
        #Todas as linhas com index Tata Motors para Nationwide, inclusive.
        #Todas colunas from rank até country, inclusive
middle_companies = f500.loc["Tata Motors":"Nationwide","rank":"country"]

## 10. Value Counts Method ##

#Nós já salvamos a seleção do data f500 com o nome de f500_sel.
    #1. Encontre os valores únicos da coluna country no dataframe f500_sel.
        #Selecione a coluna country no dataframe f500_sel. Atribua a variavel de nome countries.
        #Use o método Series.value_counts() para retornar a quantidade dos valores do countries. Atribua o resultado ao country_counts.
countries = f500_sel["country"]
country_counts = countries.value_counts()

## 11. Selecting Items from a Series by Label ##

countries = f500['country']
countries_counts = countries.value_counts()
#Do pandas Series countries_counts:
    #1. Selecione o item do index da label India. Atribua o resultado a variavel india.
    #2. Na seguinte ordem, selecione os itens com os indexs das labels USA, Canada e Mexico. Atribua o resultado a variavel de nome north_america.
india = countries_counts.loc["India"]
north_america = countries_counts.loc[["USA","Canada","Mexico"]]

## 12. Summary Challenge ##

#Selecionando dados de f500:
    #1. Criar uma nova variavel big_movers, com:
        #Linhas de indices Aviva, HP, JD.com, e BHP Billiton, esta ordem.
        #As colunas rank e previous_rank,esta ordem.
    #2. Criar uma variavel, bottom_companies,com:
        #Todas linhas com o indices National Grid ao AutoNation,inclusive.
        # E as colunas rank,sector e country.
big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"],["rank","previous_rank"]]
bottom_companies = f500.loc["National Grid":"AutoNation",["rank","sector", "country"]]