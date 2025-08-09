#Ejercicio 1
#punto 1 Crea una función que imprima "¡Bienvenido a la clase de funciones!".
def bienvenida():
    print("¡Bienvenido a la clase de funciones!")
bienvenida()

#punto 2 Crea una función que imprima tu comida favorita.
comida= input("¿Cuál es tu comida favorita? ")
def comida_favorita(comida):
    print(f"Mi comida favorita es {comida}.")

#punto 3 Crea una función que reciba un nombre y diga "Hola [nombre], ¿cómo estás?".
nombre = input("¿Cuál es tu nombre? ")
def saludar(nombre):
    print(f"Hola {nombre}, ¿cómo estás?")

#Punto 4 Crea una función que reciba una edad y diga "Tienes [edad] años."
edad = input("¿Cuál es tu edad? ")
def decir_edad(edad):
    print(f"Tienes {edad} años.")

#punto 5 Crea una función que retorne la temperatura promedio del día (puedes poner un número fijo).
def temperatura_promedio():
    return 22.5

#punto 6 Crea una función que retorne tu color favorito.
color_favorito = input("¿Cuál es tu color favorito? ")
def obtener_color_favorito():
    return color_favorito

#punto 7 Crea una función que reciba dos números y devuelva su producto.
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
def producto(num1, num2):
    return num1 * num2

#punto 8 Crea una función que reciba dos palabras y devuelva las palabras unidas.
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")
def unir_palabras(palabra1, palabra2):
    return palabra1 + palabra2



comida_favorita(comida)
saludar(nombre)
decir_edad(edad)
print(f"La temperatura promedio del día es {temperatura_promedio()}°C.")
print(f"Mi color favorito es {obtener_color_favorito()}.")
print(f"El producto de {num1} y {num2} es {producto(num1, num2):.0f}.")
print(f"Las palabras unidas son: {unir_palabras(palabra1, palabra2)}.")

