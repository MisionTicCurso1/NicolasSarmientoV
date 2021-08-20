#Ejercicio donde se pide un dato y se agreaga a una tupla
print('Marcas de tecnologia')
tp=('Samsung', 'Sony', 'Apple', 'Asus', 'Lenovo')
print(tp)

tp_1=(input('Inserte otra marca de tecnologia, la que desee: \n'),)

tp+=tp_1

print(f'Se ha incluido tu marca a la lista \n{tp}')

