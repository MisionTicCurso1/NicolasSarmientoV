#Ejercicio para intercambiar palabras

listaFrutas=['manzana','pera', 'durazno','mango','fresa','kiwi','banano','mandarina']

print(listaFrutas)
p1= input("Elija una fruta para intercambiarla \n")
p2= input()

#Hallar los indices de las palabras
p1_index= listaFrutas.index(p1.lower())
p2_index= listaFrutas.index(p2.lower())

listaFrutas.remove(p1)
listaFrutas.remove(p2)

#Intercambiarlas :)
listaFrutas.insert(p1_index,p2)
listaFrutas.insert(p2_index,p1)


print(listaFrutas)