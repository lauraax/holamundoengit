from random import randint
n1=randint(1,2)
n2=randint(1,10)
if n1>n2:
    print(n1," es mayor")
elif n2>n1:
    print(str(n2)+" es mayor")
else:
    print(str(n1)+" = "+str(n2))

