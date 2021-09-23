#Eliminacion de elementos de una lista
import random


List=[]

for a in range(0,10):
    List.append(random.randrange(0,100))

print(List)
n=int(input('Elije un numero para eliminarlo de la lista: '))

List.remove(n)

print(f'la lista nueva sin {n} es {List}')

#Otra forma que tambien funciona

# indice=List.index(n)
# List.pop(indice)
# print(f'la lista nueva sin {n} es {List}')
