#Ejercicio Para calcular el precio de un helado

#Precios

oreo= 1000
kitkat= 1500
brownie=2500
barquillo=950
prec_helado=1900

#Disponibilidad de topping
d_oreo= True
d_kitkat=True
d_brownie=True
d_barquillo=True

def helado(topping):
    global prec_helado
    if topping==1 and d_oreo== True:
        prec_helado += oreo
        print(f" Valor topping oreo...............${oreo}")
        
    elif topping==2 and d_kitkat == True:
        prec_helado += kitkat
        print(f" Valor topping KitKat.............${kitkat}")

    elif topping==3 and d_brownie == True:
        prec_helado +=  brownie
        print(f" Valor topping Brownie............${brownie}")

    elif topping==4 and d_barquillo == True:
        prec_helado +=  barquillo  
        print(f" Valor topping Barquillo..........$ {barquillo}") 

    elif topping==0:
          
        print(f" Sin topping......................$   0") 

    else:
        print(" No tenemos este topping, lo sentimos \n Sin topping......................$   0")

    return(prec_helado)

#Interfaz
print("-------------HELADERIA SINNOMBRE------------")
print("                    Menú")
print('''Helado sin topping...............$1900  (0)        
                toppings
Oreo............................. $1000 (1)
KitKat........................... $1500 (2)
Brownie.......................... $2500 (3)
Barquillo........................ $ 950 (4)
=============================================''')


#Menu
can_topp= int(input("Cuantos toppings quieres en tu helado: "))

if can_topp == 1:
    topping=int(input("Que topping desearia para su helado: "))
    print("SUBTOTAL=====================================\n Helado...........................$1900")
    helado(topping)
    print(f"TOTAL A PAGAR.....................${prec_helado}")
    print("Gracias por tu compar :)")

if can_topp == 2:
    topping=int(input("Que topping desearia para su helado: "))
    topping2=int(input("Que topping desearia para su helado: "))
    print("SUBTOTAL=====================================\n Helado...........................$1900")
    helado(topping)
    helado(topping2)
    print(f"TOTAL A PAGAR.....................${prec_helado}")
    print("Gracias por tu compar :)")

if can_topp== 3:
    topping=int(input("Que topping desearia para su helado: "))
    topping2=int(input("Que topping desearia para su helado: "))
    topping3=int(input("Que topping desearia para su helado: "))
    print("SUBTOTAL=====================================\n Helado...........................$1900")
    helado(topping)
    helado(topping2)
    helado(topping3)
    print(f"TOTAL A PAGAR.....................${prec_helado}")
    print("Gracias por tu compar :)")

if can_topp== 4:
    print("SUBTOTAL=====================================\n Helado...........................$1900")
    helado(1)
    helado(2)
    helado(3)
    helado(4)
    
    print(f"TOTAL A PAGAR.....................${prec_helado}")
    print("Gracias por tu compar :)")

if can_topp==0:
    print("SUBTOTAL=====================================\n Helado...........................$1900")
    helado(0)
    print(f"TOTAL A PAGAR.....................${prec_helado}")
    print("Gracias por tu compar :)")

if can_topp<0 or can_topp>4:
    print("comando invalido")





