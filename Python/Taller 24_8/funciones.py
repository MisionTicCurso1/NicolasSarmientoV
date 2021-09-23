#FUNCION CORREO VALIDO (1)

def correo_valido(mail):
    contador_arroba=0
    caracteres_imposibles=0

    for i in mail:   
        if i==' ':
            caracteres_imposibles+=1
            break
        
        if i=='@':
            contador_arroba+=1
    if caracteres_imposibles==1:
        print('Tu direccion es invalida, posee espacio')

    else: 
        if contador_arroba==1:
            print('tu direccion de mail es correcta')
        elif contador_arroba>1:
            print('Tu direccion es incorrecta, tiene mas de una @')
        else:
            print('Tu direccion no contiene @')

    return 0


#FUNCION EJERCICIO 2: Sumar elementos de una lista (2)
def sumalist(lista_input):
    sum=0
    for i in lista_input:
        sum+=i

    return sum


#FUNCION EJERCICIO 3: Descomponer un numero (3)
def descomposicion(num):
    lst_unidades= []
    digitos= len(str(num))
    
    for i in reversed(range(0, (digitos))):
        unidad= num//(10**i)
        num-= unidad*(10**i)
        lst_unidades.append(unidad)

    return lst_unidades


#FUNCION SABER SI UN NUMERO ES PRIMO O NO (4)
def num_primo(numero):
    
    Es_primo=True
    for i in range(2, (numero-1)):
        if numero % i== 0:
            Es_primo=False
            break

        
        
    return Es_primo


#FUNCION CONTAR DIGITOS DENTRO DE UN NUMERO (5)
def Count_digit(number, digit):


    frecuencia=0
    for i in number:
        if i== digit:
            frecuencia+=1
    
    
    return frecuencia


#FUNCION FACTORIALES (6)
def Factorials(n):
    factor=1
    factorialn=1

    while factor<=n:
        factorialn*=factor
        factor+=1

    return factorialn
