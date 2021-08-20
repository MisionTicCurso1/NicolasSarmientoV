#Ejercicio para tuplas Actualizar

rs=('facebook', 'whatsapp', 'reddit', '4chan', 'instagram', 'telegram')

l_rs= list(rs)
print('Redes sociales')
print(rs)
r1=input('Elija dos redes social para intercambiar su lugar: \n')
r2=input()

r1_index= l_rs.index(r1.lower())
r2_index= l_rs.index(r2.lower())

l_rs[r1_index]=r2
l_rs[r2_index]=r1

rs= tuple(l_rs)

print('El nuevo orden seria',rs)