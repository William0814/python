import math


# programa de para validar si aprobo el aulmo si o no

'''notaIn = float(input("Digite nota: "))
if notaIn<= 2.9:
    calificacion = "Reprobado"
else:
    calificacion = "Aprobado"
print("El alumno esta: "+calificacion)

# programa que valide si el la persona es mayor de edad o no

edad = int(input("Digite la Edad: "))
if edad <=17 :
    print("Es menor de edad con ",edad," años")
elif edad > 18 :
    print("Es mayor de edad con: ",edad," años.")
else:
    print("No ha ingresado datos")

# If abreviado

num1 = 5
num2 = 10

if num1 < num2: print(num1, "es mayor que ",num2)

#Ejemplo de operadores de comparacion concatenados

salarioP = float(input("Digite salario Presidente: "))
salarioD = float(input("Digite salario Director: "))
salarioJ = float(input("Digite salario Jefe: "))
SalarioO = float(input("Digite salario Operario: "))

if salarioP >= 4500.000 :
    print ("que buen salario!!!")
elif salarioD < salarioP:
    print("ganas menos Director")
elif salarioJ <= SalarioO:
    print ("gana mas tu Operario")
else:
    print("el Operario gana mas que el jefe!!!")'''

#Operadores AND OR

'''distanacia = float(input("Digita distancia en Metros: "))
numHermanos = int(input("Numero de hermanos en el centro: "))
nota = float(input("digite nota Promedio: "))

if distanacia >= 100 or numHermanos <=2 or nota<=2.9:
    print("No apto para beca...")
else:
    print("Es apto para beca ")'''

'''opcion = str(input("Elija una Opcion: opcion1, opcion2, opcion3, opcion4 "))
pasoMin= opcion.lower()

if pasoMin in ("opcion1", "opcion2","opcion3","opcion4"):
    print("opcion valida: "+pasoMin)
else:
    print("opcion invalida.")'''

#Programa para validar si es mayor de edad y tiene el dinero para comparar un auto

'''dinero = float(input("Cuanto dinero tienes: "))
años = int(input("Digite edad: "))
precioAuto = float(4500.00)

if dinero < precioAuto:
    print("tienes ",dinero," no te alcanza.")
else:
    if años <= 17 :
        print("Tienes el dinero pero con",años," años no puedes")
    else:
        print("Tienes ",dinero," y",años," años, puedes comprarlo")'''

#El bucle for 
for i in [1,10,30]:
    print("hola") 

for i in ["Hallo","chao","lluvia","sol"]:
    print(i)  

'''for i in "frase":
    print("hola",end=" ")
miEmail = input("Digite Email: ")
email=False
for i in miEmail:
    if i=="@":
        email = True
if email == True:
    print("correo correcto")
else:
    print("Email incorrecto: ")'''
#Podemos unir valores de texto con valores de variable a la horade imprimir.
for i in range(5):
  print(f"Valor de la variable {i}")
for i in range(5,10):
  print(f"Valor de la variable {i}")
for i in range(5,20,3):
   print(f"valor de la var {i}")

#Validar un email si en funcion de si tiene @ simplemente recorriendo la longitud del string
'''miEmail = input("Digite Email: ")
email = False

for i in range(len(miEmail)):
   if miEmail[i]=="@":
      email = True
if email:
   print(miEmail," email correcto, numero de caracteres ",i )
else:
   print("incorrecto")'''

# Con la instrucción break podemosdetener el ciclo antes de que haya pasadopor todos los elementos:
# Salga del bucle cuando x es "banana"
'''frutas = ["manzana", "banana", "cereza"]
for x in frutas:
  print(x)
  if x == "banana":
   break
  
# Con la instrucción continue podemos detener la iteración actual del ciclo y continuar con la siguiente:
# En este caso no me imprimiría "banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
  if x == "banana":
   continue
print(x)

for x in range(1,8):
   print(x)

# Bucle for anidado
# Imprime cada color para cada fruta:
color = ["verde", "amarilla", "roja"]
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
  for y in color:
   print(x, y)'''

#Pregunta la edad mientras sea negativa
'''edad = int(input("Digite edad: "))
while edad < 0:
  edad = print("Edad incorrecta.")
  edad = int(input("Digite edad:"))
print("Tienes ",str(edad))'''

'''intento =0
num = int(input("Digite numero: "))

while num<0:
  intento+=1
  print("incorrecto")
  num=int(input("Intentas de nuevo: "))
  if intento ==2:
    final= str(input("Demasiados intentos"))
    break
if num == str("n,no"):
    print("ok has terminado")
      

if intento<=2:
  intento+=1
  solucion = math.sqrt(num)
  print("La raiz cuadrada de "+str(num)+ " es: "+str(solucion))'''


#Listas

'''milista=["angel",43,55546987]
milista2= list("python")
print(milista2)

# TUPLAS
"""Una tupla es una colección ordenada e
inmutable.
En Python, las tuplas se escriben entre
paréntesis.
"""
mitupla=("manzana","banana","cereza")
print(mitupla)

mitupla2 = tuple(("manzana","banana","cereza"))
print(mitupla2)

miTupla3 = ("manzana", "banana", "cereza",
"naranja", "kiwi", "melon", "mango")
print(miTupla3[2:5])'''

# Convierta la tupla en una lista para poder cambiarla:
'''miTupla = ("manzana", "banana", "cereza")
miLista = list(miTupla)
miLista[1] = "kiwi"
miTupla = tuple(miLista)

print(miTupla)'''

miTupla1 = ("manzana", "banana", "cereza")
for x in miTupla1:
 print(x)

 # Comprobar si existe un elemento
# Compruebe si "manzana" está presente en la tupla:
miTupla2 = ("manzana", "banana", "cereza")
if "manzana" in miTupla2:
    print("Sí, manzana está en la tupla.")


miTupla = ("manzana", "banana", "cereza",12)
print(len(miTupla))

miTupla = ("manzana", "banana", "cereza"
, "manzana")
print(miTupla.count("manzana"))

# DICCIONARIOS
"""Los diccionarios, también llamados
matrices asociativas, deben su nombre a
que son
colecciones que relacionan una clave y un
valor.
Un diccionario es una colección
desordenada, modificable e indexada.
En Python, los diccionarios se escriben
entre llaves y tienen claves y valores.
"""

midiccionario = {"brand":"ford","model":"mustag","year":1965}
print(midiccionario)

# Usar una tupla dentro de un diccionario:
miDiccionario3={"nombre":"Jordan",
"Equipo":"Bulls", "Anillos":[1991, 1992,
1993, 1996, 1997, 1998]}
print(miDiccionario3["Anillos"])

# Quitar valores de un diccionario
peliculas = {"Love Actually": "Richard Curtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
peliculas.pop("Love Actually")
print(peliculas)

# Crear un diccionario a partir de dos listas:
lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
diccionario = dict(zip(lista_claves ,
lista_valores))
print(diccionario)

# SETs, conjuntos
"""
Un conjunto es una colección de elementos
únicos que no está ordenada ni indexada,
por lo que no puede estar seguro de en
qué orden aparecerán los elementos.
En Python, los conjuntos se escriben
entre llaves. Una vez que se crea un conjunto, no puede
cambiar sus elementos, pero puede agregar
nuevos elementos.
"""

# Declaración:
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo",
"Juan"}
# Otra forma de declararlo
mi_conjunto3 = set(("Angel", "Sara",
"Pilar"))
print(mi_conjunto3)

mi_conjunto.add("william")
print(mi_conjunto)
mi_conjunto.update({"isa","mime"})
print(mi_conjunto)

# FUNCIONES 
def my_funcion():
   print("ejecucion de la funcion")

my_funcion()

def suma():
   num=2
   num2=5
   print("suma= ",num+num2)
suma()
def duplica (num):
   x= num*3
   return x

print(duplica(4))

#También podríamos pasar varios valores que retornar a return.
def f(x, y):
  return x * 2, y * 2
a, b = f(1, 2)
""" Sin embargo, esto no quiere decir que
las funciones Python puedan de-volver
varios valores,
lo que ocurre en realidad es que Python
crea una tupla al vuelo cuyos elementos
son los valores a retornar, y esta única
variable es la que se devuelve."""

# Funciones con argumentos variables
# Me crea una tupla de nombre "otros"
def varios(param1, param2, **otros):
  for i in otros.items():
    print (i)
varios(1, 2, tercero =3)

"""
Crear una función para sumar los valores
recibidos de tipo numérico,
utilizando argumentos variables *args
como parámetro de la función
y regresar como resultado la suma de
todos los valores pasados como
argumentos.
"""

def suma_valores (*argumentos):
   resultado= 0
   for valor in argumentos:
      resultado+= valor
      return resultado
print(suma_valores(2,5,4,2,9,8))

def cuenta_regresiva(numero):
  numero -= 1
  if numero >= 0:
   print (numero)
   cuenta_regresiva(numero)
  else:
    print ("Boooooooom!")
    print ("Fin de la función"),
  numero
cuenta_regresiva(6)

"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total
de un pago incluyendo un impuesto
aplicado.
# Formula: pago_total = pago_sin_impuesto
+ pago_sin_impuesto * (impuesto/100)
"""

def calcular_impuesto(pago_sin_impuesto,impuesto):
   pagoTotal = pago_sin_impuesto*(impuesto/100)
   return pagoTotal
#vamos a pedir los datos para realizar el calculo
pago_sin_impuesto = float(input("pago sin puesto: "))
impuesto = float(input("Impuesto: "))
pago_con_impuesto = calcular_impuesto(pago_sin_impuesto, impuesto)
print(f"pago con impuesto:{pago_con_impuesto}")

'''Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de
grados celsius a fahrenheit y viceversa.'''


# Funcion que convierte de celsius a fahrenheit
def celcius_grados (celcius):
   return celcius * 9 / 5 +32

#funcion de farenheit a celcius
def farenheit_grados (farenheit):
   return (farenheit - 32)* 5 / 9

#realizamos la convercion de celcius a farenheit.
celcius = float(input("Digite grados celcius: "))
resultado_celcius = celcius_grados(celcius)
print(f"{celcius} C a F: {resultado_celcius:.2f}")

#realizamos la convercion de farenheit a celcius
farenheit = float(input("Digite grados farenheit: "))
resultado_farenheit = farenheit_grados(farenheit)
print(f"{farenheit} F a C: {resultado_farenheit:0.2f}")