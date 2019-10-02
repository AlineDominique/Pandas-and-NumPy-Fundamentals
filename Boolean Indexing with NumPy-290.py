## 1. Reading CSV files with NumPy ##

#1. Importe a bilblioteca Numpy atribua coomo np.
#2. Use a função numpy.genfromtxt() para ler o arquivo nyc_taxis.csv dentro do Numpy. E atribua o resultado a variavel taxi.
#3. Use o atributo ndarray.shape do taxi e atribua a variavel taxi_shape
#4. Use o inspetor de variavel abaixo do box code para visualizar o taxi ndarray e o shape apos executar o código.

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
taxi_shape = taxi.shape

## 2. Reading CSV files with NumPy Continued ##

#1. Use a função numpy.genfromtxt() novamente para ler o arquivo nyc_taxis.csv no Numpy, mas desta vez, pule a primeira linha. E atribua o resultado a variavel taxi.
#2. Atribua o shape do taxi a variavel taxi_shape
#3. Use o inspetor de variavel abaixo do box code para visualizar o taxi ndarray e o shape apos executar o código.

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv',delimiter=',',skip_header=1)
taxi_shape = taxi.shape

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

#1. Use operações booleanas vetorizadas para:
    # Avalie se os elementos no array a são menores que 3. Atribua o resultado a a_bool.
    #Avalie se os elementos no array b são iguais a "blue". Atribua o resultado a b_bool.
    #Avalie se os elementos no array c são maiores que 100. Atribua o resultado a c_bool.
#2. Use o inspetor de variavel abaixo do box code para visualizar o taxi ndarray e o shape apos executar o código.

a_bool = a < 3
b_bool = b == "blue"
c_bool = c > 100

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

#1. Calcule o número de corridas do ndarray taxi em Fevereiro:
    # Criar um array boolean, february_bool, que avalia se os itens em pickup_month são iguais a 2.
    #Use o array boolean february_bool e index ao pickup_month. E atibria o resultado ao february
    #Use o attributo ndarray.shape para encontrar o número dos termos no february. Atribua o resultado ao february_rides.
#2. Um vez que executar o código, use inspetor de variáveis para visaualizar o número de corridas de Fevereiro.

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]
#1. Criar um array boolean com o nome de tip_bool, que determine quais linhas posui valores maiores que 50 da coluna tip_amount.
#2. Use o array tip_bool para selecionar as linhas do taxi com valores maiores que 50, e as colunas do index entre 5 a 13(inclusive). Atribua o resultado ao top_tips.

tip_bool= tip_amount > 50
top_tips= taxi[tip_bool,5:14] 

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
# Para ajudar com as mudaças do  array original,nós usaremos o método ndarray.copy para taxi_modified, a copiar o original para este execercícios.
#1. O valor index da coluna pickup_location é 5, o valor index da linha está incorreto(28214). Use a atribuição para modificar o valor 1 no array taxi_modified.
#2. A primeira coluna (índice 0) contém valores do ano como números de quatro dígitos no formato AAAA (2016, pois todas as viagens em nosso conjunto de dados são de 2016). Use a atribuição para alterar esses valores para o formato YY (16) no ndarray taxi_modified.
#3. Os valores no índice da coluna 7 (trip_distance) das linhas 1800 e 1801 estão incorretos. Use a atribuição para alterar esses valores no ndarray taxi_modified para o valor médio dessa coluna.
taxi_modified[28214,5] = 1
taxi_modified[:,0] = 16
taxi_modified[1800:1802,7] = taxi_modified[:,7].mean()

## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()
# Novamente usaremoso método ndarray.copy() para fazer o array taxi_copy, para usaremos a cópia no lugar do orginal.
#1. Selecione o a coluna quatorze(index 13) no taxi_copy. E atribua a variavel de nome total_amount.
#2. Para linhas que o valor do total_amount for menor 0, mude o valor para 0.

total_amount = taxi_copy[:,13]
t_bool = total_amount < 0
total_amount[t_bool] = 0

## 8. Assignment Using Boolean Arrays Continued ##

# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)

#Nós criamos uma nova copia do dataset taxi, com o nome de taxi_modified com uma coluna adicional que contêm o valor 0 em todas as linhas.
# 1. Em nossa nova coluna no índice 15, atribua o valor 1 se o pick_location_code (índice da coluna 5) corresponder a uma localização do aeroporto, deixando o valor como 0 caso contrário, executando estas três operações:
    #Para linhas onde o valor da coluna do index 5 for igual a 2(JFK Airport), atribua o valor de 1 a coluna do index 15.
    #Para as linhas onde o valor da coluna index 5 for igual a 3(LaGauardia Airport), atribua o valor de 1 a coluna do index 15.
    #Para as linhas onde o valor da coluna index 5 for igual a 5(Newark Airport), atribua o valor de 1 a coluna do index 15.

taxi_modified[taxi_modified[:,5] == 2,15] = 1
taxi_modified[taxi_modified[:,5] == 3,15] = 1
taxi_modified[taxi_modified[:,5] == 5,15] = 1

## 9. Challenge: Which is the most popular airport? ##

#1. Usando o ndarray original taxi, calcule quantas viagens temos JFK Airport como destino.
    #Use o boolean index para selecionar as linhas onde a coluna dropoff_location_code (index 6)  tem o vlor correspondente para JFK. atribua o resultafo a variavel jfk.
    #Calcule quantas linhas tem no array jfk e atribua o resultado a variavel jfk_count.
jfk = taxi[taxi[:,6]==2]
jfk_count = jfk.shape[0]
#2. Calcule quantas viagens temos laguardia Airport como destino:
    #Use o boolean index para selecionar as linhas onde a coluna dropoff_location_code (index 6)  tem o vlor correspondente para Laguardia. Atribua o resultafo a variavel laguardia.
    #Calcule quantas linhas tem no array laguardia e atribua o resultado a variavel laguardia_count.
laguardia = taxi[taxi[:,6]==3]
laguardia_count = laguardia.shape[0]
#3. Calcule quantas viagens temos Newark Airport como destino:
    #Use o boolean index para selecionar as linhas onde a coluna dropoff_location_code (index 6)  tem o valor correspondente para Newark. Atribua o resultafo a variavel newark.
    #Calcule quantas linhas tem no array newark e atribua o resultado a variavel newark_count.
newark = taxi[taxi[:,6]==5]
newark_count = newark.shape[0]
#4. Depois execute o código e verifique pelo inspetor de variaveis qual aeroporto possui mais chegadas.


## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

#O ndarray trip_mph foi provideiciado.
trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
#1. Criar um novo ndarray, cleaned_taxi, que contenha apenas as linhas com valores do trip_mph menor que 100.
cleaned_taxi = taxi[trip_mph[:]<100]
#2. Calcule a média  da coluna trip_distance do cleaned_taxi. Atribua o resultado a variavel mean_distance.
mean_distance = cleaned_taxi[:,7].mean()
#3. Calcule a média da coluna trip_ lenght do cleaned_taxi. Atribua o resultado a variavel mean_length.
mean_length = cleaned_taxi[:,8].mean()
#4. Calcule a média do total_amount do cleaned_taxi. Atribua o resultdo a variavel mean_total_amount.
mean_total_amount = cleaned_taxi[:,13].mean()