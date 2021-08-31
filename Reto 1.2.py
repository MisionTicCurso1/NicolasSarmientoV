
'''Calcular el promedio de 5 quices y retornarlo junto con el codigo del estudiante
    Para el promedio, se debe eliminar la nota menor

    Solo hay que crea la función
'''


def nota_quices(id_estudiante,nota1,nota2,nota3,nota4,nota5):
    notas=[nota1,nota2,nota3,nota4,nota5]
    notas.sort(reverse=True)
    notas.pop()

    promedio=0

    for i in range(4):
        notas[i]/=20
        promedio+= notas[i]

    promedio/=4
    promedio= round(promedio,2)
    resultado= 'El promedio ajustado del estudiante {} es: {}'.format(id_estudiante, promedio)

    return resultado