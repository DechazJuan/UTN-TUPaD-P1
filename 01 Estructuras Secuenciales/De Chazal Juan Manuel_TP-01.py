# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

"""print("Hola Mundo!")"""

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”

"""
Nombre = input("Ingrese su nombre: ")
#print(f"Hola {Nombre}!")

"""
# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados

"""
Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Edad = int(input("Ingrese su edad: "))
Residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {Residencia}")

"""
# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro

"""
radio = float(input("Ingrese el radio de un circulo: "))
area = 3.14 * radio**2
perimetro = 2 * radio * 3.14

print(f"El area del circulo es {area} y su perimetro es {perimetro}")

"""
# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

"""
segundos = input("Ingrese una cantidad de segundos: ")
horas = float(segundos)/3600

print(f"{segundos} segundos es igual a {horas} horas")

"""
# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número

"""
numero = int(input("Ingrese un numero: "))
print(f"{numero}, {numero * 2}, {numero * 3}, {numero * 4}, {numero * 5}, {numero * 6}, {numero * 7}, {numero * 8}, {numero * 9}, {numero * 10}")"

"""
# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

"""
numero1 = int(input("ingrese el primer numero entero: "))
numero2 = int(input("ingrese el segundo numero entero: "))
suma = numero1 + numero2
resta = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2

print(f"El resultado de la suma es {suma}, el resultado de la resta es {resta}, el resultado de la multiplicacion es {mult} y de la division es {div}")"

"""
# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal

"""
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso/(altura**2)

print(f"Su IMC es igual a: {imc}")

"""
#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit

"""
tempC = float(input("Ingrese la temperatura en grados Celsius: "))
tempF = (9/5) * tempC + 32

print(f"La temperatura en grados farenheit es igual a {tempF}")

"""
#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números

"""
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))

prom = (num1 + num2 + num3)/3

print(f"El promedio de estos 3 numeros es {prom}")"

"""

a = 1
b = 2 
c = 4

A = False
B = False
C = True

r1 = (2 * b - 1) / (2 * a) > 3

r2 = a * (b * c) >= 30 and not((a+b) * c >=(350*c)) 

r3 = A and r1 or B == r2

r4 = A and B and r3 and C != r1

print(f"r1 ={r1}, r2 ={r2}, r3 ={r3}, r4 ={r4}")

