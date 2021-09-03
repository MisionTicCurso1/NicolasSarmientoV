import pandas
import numpy as nu
import random

#Ejercicio 1
print("------Ejercicio 1-----")

s1= pandas.Series([500, 3400, 900, 750], 
index=['lapiz','cuadernos','borradores','esferos'])

s1.name= 'Precios papeleria'

print(s1)

print("------Ejercicio 2-----")

datas2={
    'af': 123,
    'bc': 426,
    'nc': 90,
    'vw': 175,
    'cf': 492,
    'jk': 832
}

s2=pandas.Series(datas2)
print(s2)
#Impresion por index
print('Impresion index 2 y 4\n',s2[2],'\n', s2[4])
#Impresion por index personalizado
print('Impresion index "af" y "jk"\n',s2['af'],'\n', s2['jk'])

print("------Ejercicio 3-----")

data_dt3=nu.array([[10,13,16],[11,14,17],[12,15,18]])

DT3=pandas.DataFrame(data_dt3, index={'terna 1','terna 2','terna 3'}, columns=['A','B','C'])
DT3.index.name='Ternas'
DT3.columns.name='Letras'

print(DT3)

print("------Ejercicio 4-----")

data_dt4={
    'a1':[],
    'b1':[],
    'c1':[],
    'd1':[],
    'e1':[],
    'f1':[],
    'g1':[],
    'h1':[],
    'i1':[],
    'j1':[],
    'k1':[],
    'l1':[]
}

for i in data_dt4:
    for a in range(12):
        data_dt4[i].append(random.randint(0,200))

DT4=pandas.DataFrame(data_dt4,index={'fila 1', 'fila 2', 'fila 3', 'fila 4', 'fila 5',
'fila 6', 'fila 7', 'fila 7', 'fila 8', 'fila 9','fila 10', 'fila 11', 'fila 12'})

print(DT4)

print('\n5 primeras filas del data frame')
print(DT4.head())

print('\n5 ultimas filas del data frame')
print(DT4.tail())

print("------Ejercicio 5-----")
print('\n Informacion Dataframe 1: ')
print(DT3.info())

print('\n Informacion Dataframe 2: ')
print(DT4.info())
