'''l = list()
text = input("Digita numero: ")
if text.isnumeric():
    num = int(text)
    l.append(num)
    print("Numero: " +""+ str(num) +"  " + "añadido a la lista.")

else: 
    print("No has introducido un numero entero.")
    print(l)'''

'''d = {"5023598" : 37, "43529874" : 32}
texto = input("Digite documento: ")

    
if texto in d :
    print("la edad de " + texto+ " es " + str(d[texto])) 
    else:
    edad = input("Documento no existe. Intyroduce edad: ")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print("añadido")
    else:
        print("Dato incorrecto")

print(d)'''

import pickle
from pathlib import Path
import random 


'''file = open("myfile.pkl", "rb")
mydict = pickle.load(file)
file.close()

mydict2 = {"a" : 1, "b":2, "c":3}
output = open("myfile.pkl", "wb")
pickle.dum(mydict2, output)
output.close()'''

'''d = dict()
name = input("Digite nombre: ")
path = Path(name)
if path.is_file ():
     input_file= open(name, "rb")
     d = pickle.load(input_file)
     input_file.close()
else:
     print("El archivo no existe, creamos un diccionario vacio.")

document = input("Introduce documento: ")

if document in d:
     print("la edad de " + document + " es " + str(d[document]))
else :
     age = input("Documento no existe. introduce la edad: ")
     while age != int():
          print("Dato incorrecto solo numero.")
          break
     if age.isnumeric ():
          num = int(age)
          d[document] = num
          print("añadido. ")
     else :
          print("Dato incorrecto. Por favor introduce un numero.")

output_file = open(name, "wb")
pickle.dump (d, output_file)
output_file.close()'''

a = 0 
while a<5:
    print(a, end=" ")
    a +=1
    print(a)
print("--------------")
b = 7 
while bool(b):
    b -= 1
    if b % 2 == 0:
        continue

    print(b, end=" ")
    print(b)

c = 13
d = c // 2
while d > 1:
    if c % d == 0:
        print("{c} es factor de {d}".format(c,d))
        break
    d -= 1
else:
    print("{} es primo".format(c))

s = str("")
print("------------------")

for s in["me", "gusta","python"] :
    print (s, end=" ")

e = 0 
for x in [1,2,3,4]:
    e += x
print(e)
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values)) # Creamos el diccionario
for k in d:
    info = '{}: {}'.format(k, d[k]) # Texto formateado con claves y valores
    print(info)

letras = list("dfinewbfswaloanbsdiubaweubardvbcn")
#for c in letras:
 #   print(c, end=" ")


l1 = letras[:8]
l2 = letras[8:16]
l3 = letras[16:]

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)

for a, b, c in zip(l1,l2,l3):
    print(a + b + c, end=" ")




