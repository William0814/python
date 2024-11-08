'''import math
import random

a = random
b = random

def suma(a, b):
    if a <= b:
        print("el numero a es menor que b")
    if a >= b :
        print("el numero a es mayor que b")
    return a+b

x = suma (5,3)

print(x)'''

def suma (a, b):
    return a+b
 
x = suma (5,9)
y = suma (2.3, 2.5)
z = suma ('like','python')
print (x, '', y, '', z)

def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1

i = factorial(5)
print(factorial)

def maxmin (lista):
    return max(lista), min(lista)

o = [1,2,3,4,5,0,25]
maximo, minimo = maxmin(o)

print('minimo: ',minimo,'Maximo: ',maximo, sep= ' ')