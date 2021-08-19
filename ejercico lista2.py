#Eliminacion de elementos de una lista

List=[1,2,3,4,5,6,7,8,9,10,11]

print(List)
n=int(input('Elije un numero para eliminarlo de la lista: '))

List.remove(n)

print(f'la lista nueva sin {n} es {List}')

#Otra forma que tambien funciona

# indice=List.index(n)
# List.pop(indice)
# print(f'la lista nueva sin {n} es {List}')
