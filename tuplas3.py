#Unpacking tuples
import random

print('digitos.....')
dig_num=(0.2, 10, 23, 37,79, 92, 728, 34)

(var1, *rest,var2, var3)=dig_num

rest[2]=random.randrange(1,45)
rest[4]=random.randrange(45,90)

print(var1)
print(var2)
print(var3)
print(rest)
