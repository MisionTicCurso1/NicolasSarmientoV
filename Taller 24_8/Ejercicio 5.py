#Ejercicio 5: Contar digitos dentro de numeros y su frecuencia

from funciones import Count_digit

numero_cifras= input('Ingrese un numero de varias cifras: ')
digito= input('Ingrese un digito para encontrarlo en el anterior numero ingresado: ')

frecuencia=Count_digit(numero_cifras, digito)

if frecuencia>0:
    print(f"El numero {digito} aparece {frecuencia} veces en {numero_cifras}")
else:
    print(f"El numero {digito}, no aparece en {numero_cifras}")
