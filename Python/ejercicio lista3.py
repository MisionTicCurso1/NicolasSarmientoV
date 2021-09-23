import math


def cuadra_cubo(lista, indice):

    print(lista[indice])
    print(round((math.pow(lista[indice],2))))
    print(round((math.pow(lista[indice],3))))
    print('')
numeros=[1,2,3,4,5,6,7,8,9,10]
print('Cubos y cuadrados del 1 al 10')

for i in range(0,len(numeros)):
    cuadra_cubo(numeros, i)