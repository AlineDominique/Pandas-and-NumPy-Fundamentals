## 2. Understanding Vectorization ##

# Executar as instruções abaixo no script.py
# 1. Importe a biblioteca numpy e atibua a variavel np
# 2. Crie um Numpy ndarray com lista [10,20,30]. Atribua o resultado a variavel data_ndarray.
# 3. Click no to run para ter um feedback do código.

import numpy as np

data_ndarray = np.array([10, 20, 30])

## 3. NYC Taxi-Airport Data ##

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
#No script.py, nós usamos modulo csv do Python para importar o data nyc_taxis.csv e convertemos em lista de lista que contêm valores floats.
#1. Adiciona uma linha de código com numpy.array() para converter o dataset  coverted_taxi_list a ndarray do Numpy.
#2. Atribua o resultado a variavel taxi.

taxi = numpy.array(converted_taxi_list)


## 4. Array Shapes ##

# Todas variaveis que criamos nas missões do Dataquest da tela anterior estão disponiveis.
# 1. Atribua o valor do shape do taxi a variavel taxi_shape. E imprima o resultado.

taxi_shape = taxi.shape
print(taxi_shape)

## 5. Selecting and Slicing Rows and Items from ndarrays ##

#Para o ndarray taxi:
#1. Selecione o index 0 das linhas. Atribua ao row_0.
#2. Selecione todas as colunas do index 391 a 500(inclusive) da linhas. Atribua ao rows_391_to_500.
#3. Selecione o item do index 21 da linha e o index 5 das colunas. Atribua ao row_21_column_5

row_0 = taxi[0]
rows_391_to_500 = taxi[391:501]
row_21_column_5 = taxi[21,5]

## 6. Selecting Columns and Custom Slicing ndarrays ##

#Para o ndarray taxi:
#1. Selecione todas linhas dos indexs 1,4 e 7 das colunas.Atribua eles a columns_1_4_7
#2. Selecione os indexes do 5 ao 8(inclusive) das linhas e o index 99 das colunas. Atribua eles a row_99_columns_5_to_8
#3. Selecione os indexes do 100 ao 200(inclusive) das linhas e o index 14 das colunas. Atribua eles a rows_100_to_200_column_14

columns_1_4_7 = taxi[:,[1,4,7]]
row_99_columns_5_to_8 = taxi[99,5:9]
rows_100_to_200_column_14 = taxi[100:201,14]

## 7. Vector Math ##

fare_amount = taxi[:,9]
fees_amount = taxi[:,10]

#1. Some os vetores fare_amount e fees_amount. E atribua o resultado ao fare_and_fees.
#2. Depois execute o código, use o inspetor de variavel abaixo do code box para verificar a  varivel.

fare_and_fees = fare_amount + fees_amount

## 8. Vector Math Continued ##

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour

#1. Use a divisão de vetor para dividir trip_distance_miles por trip_length_hours e atriba o resultado ao trip_mph.
#2. Depois execute o código e use o inspetor de variaveis abaixo do code box e verifique o que contêm na nova variavel trip_mph.

trip_mph = trip_distance_miles / trip_length_hours

## 9. Calculating Statistics For 1D ndarrays ##

mph_min = trip_mph.min()
#1. Use o método ndarray.max() para calcular o valor máximo dos valores do trip_mph. E Atribua o resultado a mph_max
#2. Use o método ndarray.mean() para calcular o valor médio dos valores do trip_mph. E Atribua o resultado ao mph_mean.

mph_max= trip_mph.max()
mph_mean = trip_mph.mean()

## 11. Calculating Statistics For 2D ndarrays ##

# we'll compare against the first 5 rows only
taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13]

#Já atribuímos as cinco primeiras linhas de táxi a taxi_first_five e as quatro primeiras colunas da tabela acima a fare_components.

#Verifique se a soma de cada linha em fare_components é igual ao valor na coluna total_amount.

#1. Use o método ndarray.sum () para calcular a soma de cada linha em fare_components. Atribua o resultado a fare_sums.
#2. Extraia a 14ª coluna em taxi_first_five. Atribua a fare_totals.
#3. Imprima fare_totals e fare_sums. Use o inspetor de variáveis para verificar se os resultados correspondem. 

fare_sums = fare_components.sum(axis=1)
fare_totals = taxi_first_five[:,13]
print(fare_sums,fare_totals)