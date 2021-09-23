#Crear funcion para retornar si un numero es primo o no

from funciones import num_primo

number= int(input('Introduzca un numero para verificar si es primo o no: '))

if num_primo(number):
    print(f'{number} es primo')
else:
    print(f'{number} no es primo')
