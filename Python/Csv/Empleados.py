import pandas as pd
import csv


def Vendedores_Premiados(Vendedores):
    ventas_totales=[vendedores[1]["ventas"],vendedores[2]["ventas"],vendedores[3]["ventas"],vendedores[4]["ventas"],vendedores[5]["ventas"]]
    lista_subprom=[]
    lista_promedios=[]

    for i in range(len(ventas_totales)):
        a=0
        b=0
        for lst in ventas_totales[i]:
            if lst["devolucion"]:
                ventas_totales[i].remove(lst)
            else:
                a+=lst["ventas"]
                b+=lst["ganancias"]

        lista_subprom.append([a,b])

    for a in lista_subprom:
        promedio=0
        promedio=round(a[1]/a[0],2)
        
        lista_promedios.append(promedio)

    for p in range(len(vendedores)):
        vendedores[p+1]["promedio"]=lista_promedios[p]

    lista_promedios.sort(reverse=True)

    for x in range(len(vendedores)):
        if vendedores[x+1]["promedio"]==lista_promedios[0]:
            break

    ganador=[vendedores[x]["Nombre"],vendedores[x]["Apellidos"],vendedores[x]["Documento"],vendedores[x]["Area"]]
    
    return ganador

header_names= ["Nombres", "Apellidos", "N-Documento", "Area"]

data= pd.read_csv("Csv\Bdata.csv",header= None,
delimiter=",", names= header_names)

Nombres= data.loc[ : , "Nombres"]
Apellidos = data.loc[ : , "Apellidos"]
documento =data.loc[ : ,"N-Documento"]
Area= data.loc[ : , "Area"]


#Lista empleados
vendedores={
    1:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":[]
    },
    2:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":[]
    },
    3:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":[]
    },
    4:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":[]
    },
    5:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":[]
    },

}

#Rellenar los datos del diccionarios con CSV
for i in range(len(vendedores)):
    vendedores[i+1]["Nombre"]=Nombres[i]
    vendedores[i+1]["Apellidos"]=Apellidos[i]
    vendedores[i+1]["Documento"]=documento[i]
    vendedores[i+1]["Area"]=Area[i]
    
vendedores[1]["ventas"]=[
    {"ganancias": 1000,"ventas":2,"devolucion":False},
    {"ganancias": 1000,"ventas":2,"devolucion":False},
    {"ganancias": 1000,"ventas":2,"devolucion":True},
]
vendedores[2]["ventas"]=[
    {"ganancias": 1200,"ventas":4,"devolucion":False},
    {"ganancias": 1820,"ventas":3,"devolucion":True},
    {"ganancias": 9120,"ventas":2,"devolucion":True},
]
vendedores[3]["ventas"]=[
    {"ganancias": 1238,"ventas":1,"devolucion":False},
    {"ganancias": 432,"ventas":2,"devolucion":False},
    {"ganancias": 190,"ventas":3,"devolucion":True},
]
vendedores[4]["ventas"]=[
    {"ganancias": 829,"ventas":1,"devolucion":False},
    {"ganancias": 823,"ventas":2,"devolucion":False},
    {"ganancias": 728,"ventas":2,"devolucion":True},
]
vendedores[5]["ventas"]=[
    {"ganancias": 921,"ventas":6,"devolucion":False},
    {"ganancias": 1723,"ventas":1,"devolucion":False},
    {"ganancias": 937,"ventas":3,"devolucion":False},
]



print(Vendedores_Premiados(vendedores))
