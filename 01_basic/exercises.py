###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

# print("\nEjercicio 1: Imprimir mensajes")
# print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# ### Completa aquí

# nombre = input("Escribe tu nombre: ")
# ciudad = input("Escribe tu ciudad: ")   

# print(f"Tu nombre es {nombre}\nVives en {ciudad}")

# print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
# print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
# a = 15
# b = 3.14159
# c = "Hola mundo"
# d = True
# e = None

# ### Completa aquí
# print(type(a), type(b), type(c), type(d), type(e))

# print("\nEjercicio 3: Casting de tipos")
# print("Convierte la cadena \"12345\" a un entero y luego a un float.")
# print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

# ### Completa aquí

# entero = (int("12345"))
# print(entero)
# float = (float(entero))
# print(float)

# print(int(3.99))

# # 3.99 en entero se convierte en 3, se pierde la parte decimal

# print("\nEjercicio 4: Variables")
# print("Crea variables para tu nombre, edad y altura.")
# print("Usa f-strings para imprimir una presentación.")

# # "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

# ### Completa aquí

# nombre = "Damian"
# Edad = 35
# Altura = 1.75

# print(f"Hola! Me llamo {nombre} y tengo {Edad} años, mido {Altura} metros")

# print("\nEjercicio 5: Números")
# print("1. Crea una variable con el número PI (sin asignar una variable)")
# print("2. Redondea el número con round()")
# print("3. Haz la división entera entre el número que te salió y el número 2")
# print("4. El resultado debería ser 1")

# PI = 3.14159
# rounded = round(PI)
# division = int(rounded / 2)
# print(rounded, division)