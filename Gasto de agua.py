#Ejercicio para cobrar el consumo de H2O
print(".........Cobro de agua por m^3............")
a= int(input("Ingrese su consumo de agua en m^3: "))

#Cobrar los primeros 100
if a>100:
    a-=100
    cobro=100*10
else:
    cobro=a*10

#Descomponemos el valor en unidades m, centenas, decenas y unidades
um = a//1000
a-= (um*1000)
c= a//100
a-= (c*100)
d= a//10
a-= (d*10)
u=a

#Evaluamos los valores descompuestos

if um>=1:
    um*=1000
    cobro+=um*90

c= (c*100)+(d*10)+ u

#Los numeros de 3 cifras van del 0 hasta el 999
if 1<=c<=500: #Intervalo de 100 a 500
    cobro+=c*25
if 500<c<=999: #Intervalo de 500 a 1000
    cobro+=c*50
    
print("El total a pargar por su consumo es de $",cobro)
