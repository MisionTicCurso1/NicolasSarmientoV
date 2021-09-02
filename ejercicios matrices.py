import numpy as np

m1= np.random.randint(50, size=(5,2))
m2= np.array([[3,4],[64,12],[22,1],[18,53],[9,30]])
print("matriz 1 \n",m1,"\n","matriz 2 \n", m2)

#Suma
print("Suma \n", np.add(m1,m2))
#Resta
print("Resta \n", np.subtract(m1,m2))
#Multiplicacion
print("multiplicacion \n", np.multiply(m1,m2))
#Division
print("division \n", np.divide(m1,m2))

print("\n\n-------------------------------\nEjercicio2: \n")
m3=np.random.random((4,3))
print("matriz 3 \n", m3)
m3= np.fliplr(m3)
print("matriz3 con columnas invertidas \n",m3)

print("\n\n-------------------------------\nEjercicio3: \n")
mp1=np.random.randint(40, size=(4,4))
mp2=np.random.randint(40, size=(4,4))
print(f"matriz 1\n{mp1}\nmatriz 2\n {mp2}\n", mp1.dot(mp2))

print("\n\n-------------------------------\nEjercicio 4: \n")

Ma=np.random.random((3,3))
Mbr=np.random.randint(10, size=3)
print(f"matriz 1\n{Ma}\nmatriz 2\n {Mbr}\n", Ma+Mbr)

print("\n\n-------------------------------\nEjercicio 5: \n")

M6x6=np.random.randint(20, size=(6,6))
print(f"Matriz 6x6: \n {M6x6}\n")

print("Fila 2 en adelante \n",M6x6[2:],"\n")
print("La columna 3 de todas las filas \n",M6x6[: ,3],"\n")
print("Fila 0 hasta la 2, con todas las filas: \n",M6x6[0:2])
