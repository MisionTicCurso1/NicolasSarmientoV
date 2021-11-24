def Fibonacci(number):
    if number==0 or number==1:
        return number
    return Fibonacci(number-1)+Fibonacci(number-2)

for i in range(40):
    print(Fibonacci(i))