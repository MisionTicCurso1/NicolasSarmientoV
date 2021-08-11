#ejercicio que calcula el IMC y lo clasifica

print("Programa para calcular el IMC y lo clasifica")


#Declaramos M como Masa y A como altura, siendo flotantes... porque pueden ser variables decimales
M= float(input("Ingrese por favor su masa en KG: "))
A= float(input("Ingrese su altura por favor en M: "))

#Realizamos el calculo del IMC,agregamos el ** para realizar la exponenciación
IMC=round((M/(A**2)),2)

#Clasificamos la variable IMC según los parametros, usando condicionales
if IMC <18.5:
    print(f"su IMC es: {IMC} clasificado como peso bajo")

if IMC >= 18.5 and IMC <= 24.9:
    print(f"su IMC es: {IMC} clasificado como peso normal")

if IMC>= 25 and IMC <= 29.9:
    print(f"su IMC es: {IMC} clasificado como sobrepeso")

if IMC >= 30 and IMC <= 34.9:
    print(f"su IMC es: {IMC} clasificado como obesidad tipo I")

if IMC >= 35 and IMC <=39.9:
    print(f"su IMC es: {IMC} clasificado como obesidad tipo II")
    
if IMC >=40:
    print(f"su IMC es: {IMC} clasificado como obesidad tipo III")

#Mensaje de decoración
print("Cuida tu salud :)")

