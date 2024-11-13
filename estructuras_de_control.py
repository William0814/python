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

