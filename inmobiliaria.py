#Ejercicio de Listas y Diccionarios



def calculoInmuebles(lista_mob, precio):
    lista_fin=[]

    for i in lista_mob:
        
        costo= ((i["metros"]*1000)+ (i["habitaciones"]*5000))
        if i["garaje"]==True:
            costo+=15000

        if i["zona"]== "A":
            costo*= ((2021-i["año"])/100)
        
        if i["zona"]== "B":
            costo*= (((2021-i["año"])/100))*1.5

        i["costo"]= round(costo,1)

        if costo <= precio:
            lista_fin.append(i)

    return lista_fin   
   
        

inmuebles= [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

presupuesto= int(input("Presupuesto para su inmueble: "))

for i in calculoInmuebles(inmuebles, presupuesto):
    print(i)
    

