"""#Ejercicio 1
#punto 1 Crea una función que imprima "¡Bienvenido a la clase de funciones!".
def bienvenida():
    print("¡Bienvenido a la clase de funciones!")
bienvenida()

#punto 2 Crea una función que imprima tu comida favorita.
comida= input("¿Cuál es tu comida favorita? ")
def comida_favorita(comida = "pizza"):
    print(f"Mi comida favorita es {comida}.")

#punto 3 Crea una función que reciba un nombre y diga "Hola [nombre], ¿cómo estás?".
nombre = input("¿Cuál es tu nombre? ")
def saludar(nombre = "Yonatan"):
    print(f"Hola {nombre}, ¿cómo estás?")

#Punto 4 Crea una función que reciba una edad y diga "Tienes [edad] años."
edad = input("¿Cuál es tu edad? ")
def decir_edad(edad = 25):
    print(f"Tienes {edad} años.")

#punto 5 Crea una función que retorne la temperatura promedio del día (puedes poner un número fijo).
def temperatura_promedio():
    return 22.5

#punto 6 Crea una función que retorne tu color favorito.
color = input("¿Cuál es tu color favorito? ")
def obtener_color_favorito(colorFavorito = "Negro"):
    return colorFavorito

#punto 7 Crea una función que reciba dos números y devuelva su producto.
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
def producto(num1 = 5, num2 = 6):
    return num1 * num2

#punto 8 Crea una función que reciba dos palabras y devuelva las palabras unidas.
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")
def unir_palabras(palabra1 = "Hola", palabra2 = "Mundo"):
    return palabra1 + palabra2

#Llamado de funciones
comida_favorita(comida)
saludar(nombre)
decir_edad(edad)
print(f"La temperatura promedio del día es {temperatura_promedio()}°C.")
print(f"Mi color favorito es {obtener_color_favorito(color)}.")
print(f"El producto de {num1} y {num2} es {producto(num1, num2):.0f}.")
print(f"Las palabras unidas son: {unir_palabras(palabra1, palabra2)}.")

#crear una lista que sume 5 elementos y 10
def sumar_for (*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma
print(f"La suma de los números es: {sumar_for(1, 2, 3, 4, 5, 10,34, 56, 78)}")"""

#Ejercicio 2 solo usando sorted, map, filter y lambda

#punto 1 Dada una lista de temperaturas en grados Celsius, usar map y lambda para convertirlas a grados Fahrenheit. Fórmula: F = C * 1.8 + 32
temperaturas_celsius = [0, 20, 37, 100]
temperaturas_fahrenheit = list(map(lambda c: c * 1.8 + 32, temperaturas_celsius))
print(f"Temperaturas en Fahrenheit: {temperaturas_fahrenheit}")

#punto 2 Dada una lista de números, usar map y lambda para obtener el cubo de cada número.
numeros = [1, 2, 3, 4, 5]
cubos = list(map(lambda x: x ** 3, numeros))
print(f"Cubos de los números: {cubos}")

#Punto 3 De una lista de palabras, usar filter y lambda para obtener solo las palabras que tengan más de 5 letras.
palabras = ["Python", "JavaScript", "C", "Java", "Ruby", "PHP"]
palabras_largas = list(filter(lambda x: len(x) > 5, palabras))
print(f"Palabras con más de 5 letras: {palabras_largas}")

#punto 4 De una lista de números, usar filter y lambda para quedarte únicamente con los números pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {numeros_pares}")

#punto 5 Dada una lista de tuplas con el formato (nombre, edad), usar sorted y lambda para ordenarlas de menor a mayor edad.
tuplas = [("Juan", 25), ("Ana", 22), ("Pedro", 30), ("Maria", 20)]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print(f"Tuplas ordenadas por edad: {tuplas_ordenadas}")

#Punto 6 Dada una lista de productos con el formato (nombre, precio), usar sorted y lambda para ordenarlos de mayor a menor precio.
productos = [("Manzana", 1200), ("Banana", 600), ("Naranja", 800), ("Pera", 1000), ("Uva", 1500), ("Kiwi", 2000)]
productos_ordenados = sorted(productos, key=lambda x: x[1], reverse=True)
print(f"Productos ordenados por precio de mayor a menor: {productos_ordenados}")


