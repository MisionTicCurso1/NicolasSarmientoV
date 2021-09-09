import pandas as pd
import csv


def Vendedores_Premiados(Empleados):
    ventas_validas=[]
    for id in range(len(Empleados)):
        if not Empleados[id+1]["ventas"]["Devolucion"]:
            Empleados[id+1]["ventas"]["ventas"]-=1

    for i in range(len(Empleados)):
        Empleados[i+1]["Promedio_ventas"]=(Empleados[i+1]["ventas"]["ganancias"]/ Empleados[i+1]["ventas"]["ventas"])
        ventas_validas.append(Empleados[i+1]["Promedio_ventas"])
        

    ventas_validas.sort(reverse=True)
    for x in range(len(Empleados)):
        if ventas_validas[0]==Empleados[x+1]["Promedio_ventas"]:
            break
        
    premiados= [Empleados[x+1]]
    return premiados

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
        "ventas":{
            "ganancias": 300000,
            "ventas": 20,
            "Devolucion": False
        }
    },
    2:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":{
            "ganancias": 123000,
            "ventas": 30,
            "Devolucion": True
        }
    },
    3:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":{
            "ganancias": 23000,
            "ventas": 50,
            "Devolucion": False
        }
    },
    4:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":{
            "ganancias": 903000,
            "ventas": 10,
            "Devolucion": True
        }
    },
    5:{ "Nombre": "",
        "Apellidos": "",
        "Documento": 0,
        "Area": "",
        "ventas":{
            "ganancias": 10,
            "ventas": 20,
            "Devolucion": False
        }
    },

}

#Rellenar los datos del diccionarios con CSV
for i in range(len(vendedores)):
    vendedores[i+1]["Nombre"]=Nombres[i]
    vendedores[i+1]["Apellidos"]=Apellidos[i]
    vendedores[i+1]["Documento"]=documento[i]
    vendedores[i+1]["Area"]=Area[i]
    

print(Vendedores_Premiados(vendedores))

