#Ejercicio 3: Suma de digitos
from funciones import sumalist, descomposicion

num= 1
list_nums=[]
print('Ingrese numeros para sumarlos, para detener el procesos, ingrese el "0" \nIngrese un numero numero: ')

while num != 0:
    num= int(input())
    list_nums.append(num)

list_nums.pop()
print('==================================')
for i in list_nums:
    print(i,'=',sumalist(descomposicion(i)))


