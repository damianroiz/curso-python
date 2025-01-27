###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os

print("\n Sentencia simple condicional")

edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 5

if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 16
tiene_carnet = True

# JavaScript
# && -> and
# || -> or

# 🇻🇪 un pueblo de Valencia
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")

# 🇻🇪 un pueblo de Isla Margarita
if edad >= 18 or tiene_carnet:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")

es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
  print("¡midu, venga que hay que streamear!")


print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

# Más fácil:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

numero = 5
if numero: # True
  print("El número no es cero")

numero = 0
if numero: # False
  print("Aquí no entrará nunca")

nombre = ""
if nombre:
  print("El nombre no es vacío")

numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")


print("\nLa condición ternaria:")
# es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)


os.system("clear")

###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# firstNumber = int(input("Introduce el primer número: "))
# secondNumber = int(input("Introduce el segundo número: "))

# if firstNumber > secondNumber:
#   print(f"El primer número ({firstNumber}) es mayor que el segundo número ({secondNumber})")
# elif firstNumber < secondNumber:
#   print(f"El segundo número ({secondNumber}) es mayor que el primer número ({firstNumber})")  
# else:
#   print("Ambos numeros son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# firstNumber = int(input("Introduce el primer numero: "));
# secondNumber = int(input("Introduce el segundo numero: "));
# operation = input("Introduce la operacion (+, -, *, /): ");

# if operation == "+":
#   print(f"El resultado de la suma es: {firstNumber + secondNumber}")
# elif operation == "-":
#   print(f"El resultado de la resta es: {firstNumber - secondNumber}")
# elif operation == "*":
#   print(f"El resultado de la multiplicacion es: {firstNumber * secondNumber}")
# elif operation == "/":
#   if secondNumber == 0:
#     print("No se puede dividir por cero")
#   else:
#     print(f"El resultado de la division es: {firstNumber / secondNumber}")



# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# year = int(input("Introduce un año: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#   print(f"El año {year} es bisiesto")
# else: 
#   print(f"El año {year} no es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("Introduce tu edad: "))

if age >= 0 and age <= 2:
  print("Eres un bebé")
elif age >= 3 and age <= 12:
  print("Eres un niño")
elif age >= 13 and age <= 17:
  print("Eres un adolescente")
elif age >= 18 and age <= 64:
  print("Eres un adulto")
elif age >= 65 <= 110:
  print("Eres un adulto mayor")
else:
  print("Edad no válida")
