#Ejericicio 6 Factoriales
from funciones import Factorials


print('Ejercicio para calcular factoriales \nIngrese la cantidad de factoriales a obtener: ')
cant_factorial= int(input())
nf=[]
f=[]
print('Escriba sus numeros...')
for i in range(cant_factorial):
    f.append(int(input()))
    nf.append(Factorials(f[i]))

for x in range(0, len(f)):
    print(f[x],'! =',nf[x])