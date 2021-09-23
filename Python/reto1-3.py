data={
    20170136837:{
        'nombres':'Jorge Juan',
        'apellidos':'Moreno, López',
        'documento':1058327925,
        'programa':'ARQU',
        'materias':[
            {
                'facultad':'Arquitectura',
                'codigo':'ARQUI-2113',
                'nota':2.97,
                'creditos':0,
                'retirada':'No'

            },
            {
                'facultad':'Arquitectura',
                'codigo':'ARQUI-2113',
                'nota':4.71,
                'creditos':0,
                'retirada':'No'
            }
        ]
    },
    20140136837:{
        'nombres':'Láurá Helena',
        'apellidos':'Moreno, Garcia',
        'documento':1058327925,
        'programa':'ARQU',
        'materias':[
            {
                'facultad':'Arquitectura',
                'codigo':'ARQUI-2113',
                'nota':2.97,
                'creditos':2,
                'retirada':'No'

            },
            {
                'facultad':'Arquitectura',
                'codigo':'ARQUI-2113',
                'nota':2.1,
                'creditos':4,
                'retirada':'No'
            },
            {
                'facultad':'Arquitectura',
                'codigo':'ARQUI-2113',
                'nota':2.8,
                'creditos':4,
                'retirada':'No'
            }
        ]
    },
    2019312890:{
        'nombres':'Enrique Juan',
        'apellidos':'Sotaquira, Rodriguez',
        'documento':1058327925,
        'programa':'ARQU',
        'materias':[
            {
                'facultad':'Arquitectura',
                'codigo':'ARQUI-2113',
                'nota':2.97,
                'creditos':2,
                'retirada':'No'

            },
            {
                'facultad':'Arquitectura',
                'codigo':'ARQUI-2113',
                'nota':2.1,
                'creditos':4,
                'retirada':'No'
            },
            {
                'facultad':'Arquitectura',
                'codigo':'ARQUI-2113',
                'nota':2.8,
                'creditos':4,
                'retirada':'No'
            }
        ]
    }
}
def Seleccion(info:dict)->list:
    materias=[]
    id_est=[]



    for i in info:
        notas_est={}
        notas_est['id']=i
        notas_est['notas']=[]
        notas_est['creditos']=[]

        for nm in range(len(info[i]['materias'])):
            if info[i]['materias'][nm]['retirada']=='No':
                notas_est['notas'].append(info[i]['materias'][nm]['nota'])
                notas_est['creditos'].append(info[i]['materias'][nm]['creditos'])
                

        materias.append(notas_est)

    for l in materias:
        f1=0
        f2=0
        prom=0

        for notas in range(len(l['notas'])):
            f1+=l['notas'][notas]*l['creditos'][notas]
            f2+=l['creditos'][notas]

        if f2==0:
            prom=0
        else:
                prom=f1/f2 

        l['promedio']=round(prom,2) 

    list_prom=[]

    for p in materias:
        list_prom.append(p['promedio'])

    list_prom.sort(reverse=True)
    promedio_ganador=list_prom[0]

    for em in materias:
        if em['promedio']==promedio_ganador:
            id_est.append(str(em['id']))

    id_est.sort()
    id_ganador=int(id_est[0])

    nomb_ganador=info[id_ganador]['nombres']


    for letra in range(len(info[id_ganador]['apellidos'])):
        if info[id_ganador]['apellidos'][letra]==',':
            break
            
    apellido2_ganador=info[id_ganador]['apellidos'][0:letra]
    apellido1_ganador=info[id_ganador]['apellidos'][letra+2:]
    apellidos_ganador=apellido1_ganador+' '+apellido2_ganador
    digitos=str(info[id_ganador]['documento'])

    digitos=digitos[-2]+digitos[-1]

    if ' ' in nomb_ganador:
        for letter in range(len(nomb_ganador)):
            if nomb_ganador[letter]==' ':
                break

        correo=nomb_ganador[0]+nomb_ganador[letter+1]+'.'+apellido1_ganador+digitos
    else:
        correo=nomb_ganador[0]+apellido1_ganador[0]+'.'+apellido2_ganador+digitos

    transl=correo.maketrans('áéíóúñ','aeioun')
    correo=correo.translate(transl)


    ganador=[id_ganador, nomb_ganador, apellidos_ganador,info[id_ganador]['documento'],
    info[id_ganador]['programa'],promedio_ganador, correo.lower()]
    return ganador


print(Seleccion(
{   
    20130225137:{
        "nombres" : "Sara Carolina",
        "apellidos" : "Gómez, Fernández",
        "documento" : 58770043,
        "programa" : "ARQD",
        "materias" : [
            {
                "facultad" : "Arquitectura",
                "codigo" : "ARQU-8218",
                "nota" : 4.49,
                "creditos" : 2,
                "retirada" : "No",
            },
            {
                "facultad" : "Arquitectura",
                "codigo" : "ARQU-2113",
                "nota" : 2.97,
                "creditos" : 2,
                "retirada" : "Si",
            },
            {
                "facultad" : "Arquitectura",
                "codigo" : "ARQU-5048",
                "nota" : 4.26,
                "creditos" : 2,
                "retirada" : "No",
            },
        ]
    },
    20170136837:{
        "nombres" : "Jorge Juan",
        "apellidos" : "Moreno, López",
        "documento" : 88481595,
        "programa" : "ARQU",
        "materias" : [
            {
                "facultad" : "Arquitectura",
                "codigo" : "ARQU-8218",
                "nota" : 4.49,
                "creditos" : 2,
                "retirada" : "No",
            },
            {
                "facultad" : "Arquitectura",
                "codigo" : "ARQU-2113",
                "nota" : 2.97,
                "creditos" : 2,
                "retirada" : "Si",
            },
            {
                "facultad" : "Arquitectura",
                "codigo" : "ARQU-5048",
                "nota" : 4.26,
                "creditos" : 2,
                "retirada" : "No",
            },
        ]
    },
        
    20110274333:{
        "nombres" : "Carolina Paula",
        "apellidos" : "Ochoa, López",
        "documento" : 82364435,
        "programa" : "DIMD",
        "materias" : [
            {
                "facultad" : "Diseño",
                "codigo" : "DIMD-7972",
                "nota" : 3.15,
                "creditos" : 1,
                "retirada" : "No",
            },
            {
                "facultad" : "Diseño",
                "codigo" : "DIGR-9331",
                "nota" : 4.0,
                "creditos" : 3,
                "retirada" : "No",
            },
            {
                "facultad" : "Medicina",
                "codigo" : "MEDI-8548",
                "nota" : 3.1,
                "creditos" : 3,
                "retirada" : "No",
            },
        ]
    },
    20200116062:{
        "nombres" : "Sara Camila",
        "apellidos" : "Martínez, Gómez",
        "documento" : 40079000,
        "programa" : "DIGR",
        "materias" : [
            {
                "facultad" : "Diseño",
                "codigo" : "DIGR-9331",
                "nota" : 4.0,
                "creditos" : 3,
                "retirada" : "No",
            },
            {
                "facultad" : "Diseño",
                "codigo" : "DIGR-3530",
                "nota" : 3.4,
                "creditos" : 3,
                "creditos" : 3,
                "retirada" : "No",
            },
            {
                "facultad" : "Arquitectura",
                "codigo" : "ARQU-2113",
                "nota" : 3.9,
                "creditos" : 2,
                "retirada" : "No",
            },
            {
                "facultad" : "Arquitectura",
                "codigo" : "ARQU-1221",
                "nota" : 4.37,
                "creditos" : 4,
                "retirada" : "No",
            }
        ]
    },
    20160219974:{
        "nombres" : "Daniela Sara",
        "apellidos" : "Cuellar, Guitiérrez",
        "documento" : 80398132,
        "programa" : "IIND",
        "materias" : [
            {
                "facultad" : "Ingenieria",
                "codigo" : "IIND-3557",
                "nota" : 3.91,
                "creditos" : 1,
                "retirada" : "No",
            },
            {
                "facultad" : "Ingenieria",
                "codigo" : "IIND-5158",
                "nota" : 3.83,
                "creditos" : 3,
                "retirada" : "No",
            },
            {
                "facultad" : "Ingenieria",
                "codigo" : "IIND-7543",
                "nota" : 3.41,
                "creditos" : 3,
                "retirada" : "No",
            }
        ]
    }
}))
