import pandas
import csv


#Ejercicio 1

pandas.set_option('display.max_rows',99)
pandas.set_option('display.max_columns',99)
pandas.set_option('display.width',5000)

# cvs1=pandas.read_csv('CSV10.csv', header=None, encoding='unicode_escape')
# cvs2=pandas.read_csv('CSV100.csv', header=None, encoding='unicode_escape')

# print(cvs1)
# print('')
# print(cvs2)

#Ejercicio 2

hd_names=['col1','col2','col3']
data=pandas.read_csv('Data.csv', header=None, encoding='unicode_escape',
names=hd_names)

col1=data.loc[ : , 'col1']
col2=data.loc[ : , 'col2']
col3=data.loc[ : , 'col3']

data['col4']= col1+col2
data['col5']= col2+col3
data['col6']= col3*(col2+col3)



print(data)

#Ejercicio 3

titles=['nota 1', 'nota 2', 'nota 3', 'nota 4']
periodo1=[[5 , 3, 4.2 , 4.5], [3, 3.2 , 4.3 , 5], [2 , 3.9, 4.3, 5],[5 , 1, 4.2, 3.1]]

with open('escritura.csv', 'w', encoding='UTF8') as notas:
    escritura=csv.writer(notas)

    escritura.writerow(titles)
    for l in periodo1:
        escritura.writerow(l)

esc_show=pandas.read_csv('escritura.csv', header=0, encoding='UTF8')
print('')

print(esc_show)