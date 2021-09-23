#Ejercio 2 Pedir numeros hasta que ingresen 0, luego hacer la suma de todos los numeros

from funciones import sumalist

num= 1
list_nums=[]
print('Ingrese numeros para sumarlos, para detener el procesos, ingrese el "0" \nIngrese un numero numero: ')

while num != 0:
    num= int(input())
    list_nums.append(num)

print(sumalist(list_nums))