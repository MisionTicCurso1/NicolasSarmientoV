#Ejercicio para intercambiar palabras
import random


Frutas=['manzana','pera', 'durazno','mango','fresa','pomarrosa',
'durazno','melon','guayaba','sandia','limon','uva','maracuyá','curuba','tamarindo',
'frambuesa','toronja','albaricoque','membrillo','dátil','carambola','cereza']

listaFrutas=[]

for i in range(0,6):
    listaFrutas.append(random.choice(Frutas))


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