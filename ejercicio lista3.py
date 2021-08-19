import math


def cuadra_cubo(lista, indice):

    print(lista[indice])
    print(round((math.pow(lista[indice],2))))
    print(round((math.pow(lista[indice],3))))
    print('')




numeros=[1,2,3,4,5,6,7,8,9,10]

print('Cubos y cuadrados del 1 al 10')

cuadra_cubo(numeros,0)
cuadra_cubo(numeros,1)
cuadra_cubo(numeros,2)
cuadra_cubo(numeros,3)
cuadra_cubo(numeros,4)
cuadra_cubo(numeros,5)
cuadra_cubo(numeros,6)
cuadra_cubo(numeros,7)
cuadra_cubo(numeros,8)
cuadra_cubo(numeros,9)