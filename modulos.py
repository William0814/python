import math

'''Solicitando elementos de List/Set uno
por uno
Para introducir los elementos de la Lista/Set uno por
uno usaremos el método append() en el caso de las
Listas, y el método add() en el caso de los conjuntos'''
#-------------------------------------------------------
'''a, b, c = map(int,input("digite numeros: ").split())
print("Los numero son: ",end=" ")
print(a, b, c)

List = list(map(int, input("Digite los elementos de la lista: ").split()))
Set = set(map(int, input("Digite los elementos del set: ").split()))

l = int(input("Digite nnumero del tamamño en la lista: "))
s = int(input("Digite numero de tamaño del set: "))
print("Introdusca los elementos de la lista")

for i in range(0, 1):
    list.append(int(input()))
print("Digite los elementos del sed:")
for i in range(0, 5):
    set.add(int(input()))
print(List)
print(Set)

T = (2,3,4,5,6,7)

print("Tupla inicial: ")
print(T)
L = list(T)
L.append(int(input("Digite nuevo elemento:")))
L = tuple(L)
print("Tupla final ")
print(L)'''
#--------------------------------------------------

print("isa","willi","kari","emi", sep="/")
print ("isa","willi","kari","emi", end="*")

'''Uso de literales de cadena
formateados
Podemos usar literales de cadena con formato,
comenzando una cadena con f o F antes de abrir
comillas o comillas triples. En esta cadena, podemos
escribir expresiones de Python entre { } que pueden
referirse a una variable o cualquier valor literal.'''

name = "william"

print(f"Mi nombre es {name}",name)
#-------------------------------------------------

'''Usando format()
También podemos usar la función format() para
formatear nuestra salida para que se vea
presentable. Las llaves { } funcionan como
marcadores de posición. Podemos especificar el
orden en que aparecen las variables en la salida.
Ejemplo: formato de cadena de Python usando la
función format()'''

a = 20
b = 20

sum = a+b
sub = a-b

print("El valor de a es {} y b es {}".format(a,b))
print("La suma de a + b es {}".format(sum))
print("{sub} es la resta de {a} y {b}".format(sub=sub,a=a,b=b))


