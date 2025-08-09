#Integrantes: Laura cuellar, Yonatan Diaz
#Punto 1 Solicita al usuario ingresar 8 números enteros distintos y almacénalos en una lista llamada `numeros`.
print("\nPunto 1")
import random
numeros = []

"""for i in range(1,9):
    numeros.append(random.randint(1,100))"""

for i in range(1,9):
    while True:
        numero = (input(f"Ingrese el número {i}: "))
        if numeros.__contains__(int(numero)):
            print("El número ya existe")
        else:
            esNumero = numero.isdigit()
            if esNumero:
                numeros.append(int(numero))
                break
            else:
                print("Ingresa solo números enteros")
print(f"Lista de números: {numeros}")
#Punto 2 Crea una tupla llamada `referencia` con los mismos 8 valores pero ordenados de menor a mayor.
print("\nPunto 2")
referencia = tuple(sorted(numeros))
print(f"Los números ordenados son: {referencia}")
# Punto 3 Crea un diccionario llamado `clasificacion` que asocie cada valor de la lista `numeros` con "par" o "impar", según corresponda.
print("\nPunto 3")
clasificacion = {"Par": [] , "Impar": []}
for i in numeros:
    if i % 2 == 0:
        clasificacion["Par"].append(i)
    else:
        clasificacion["Impar"].append(i)
print(f"La clasificación de los números es: {clasificacion}")
#Punto 4 Imprime todos los pares encontrados en el diccionario `clasificacion`.
print("\nPunto 4")
print(f"Los números pares son: {clasificacion['Par']}")
#Punto 5 Crea un conjunto llamado `impares_mayores` que contenga los valores impares de `numeros` que sean mayores que 10.
print("\nPunto 5")
impares_mayores = set()
for i in clasificacion["Impar"]:
    if i> 10:
        impares_mayores.add(i)
print(f"Los números impares mayores a 10 son: {impares_mayores}")
#Punto 6 Imprime todos los elementos del conjunto `impares_mayores` que también estén en la tupla `referencia`.
print("\nPunto 6")
print("Los elementos repetidos que tambien estan en el conjunto 'impares_mayores' son:", end=" ")
for i in referencia:
    for n in impares_mayores:
        if i == n:
            print(n , end=", ")
print("\n")
#Punto 7 Usando solo ciclos y condicionales, encuentra el mayor valor impar de la lista `numeros` y el menor valor par.
print("\nPunto 7")
suma = 0
for i in numeros:
    suma += i
promedio = suma / len(numeros)
mayorImpar = menorPar = promedio
for i in numeros:
    if i > mayorImpar and i % 2 != 0:
        mayorImpar = i
    elif i < menorPar and i % 2 == 0:
        menorPar = i
print(f"El número mayor impar es: {mayorImpar}")
print(f"El número menor par es: {menorPar}")
#Punto 8 Crea una lista `cuadrados` que contenga el cuadrado de cada número en la lista original `numeros`.
print("\nPunto 8")
cuadrados = []
for i in numeros:
    cuadrados.append(i * i)
print(f"El cuadrado de cada número en la lista 'numeros' es: {cuadrados}")
#Punto 9 Recorre la lista `cuadrados` y crea un conjunto con todos los resultados que sean múltiplos de 5 y mayores a 30.
print("\nPunto 9")
multiplos_5_mayores_30 = set()
for i in cuadrados:
    if i % 5 == 0 and i > 30:
        multiplos_5_mayores_30.add(i)
print(f"Los números multiplos de 5 y mayores a 30 de las lista cuadrados son: {multiplos_5_mayores_30}")
#Punto 10 Crea un nuevo diccionario `cuadrado_estado` que asocie cada número original con "alto" si su cuadrado supera 100, y "bajo" si no.
print("\nPunto 10")
cuadrado_estado = {"Alto": [], "Bajo": []}
for i in numeros:
    if i * i > 100:
        cuadrado_estado["Alto"].append(i)
    else:
        cuadrado_estado["Bajo"].append(i)
print(f"Los cuadrados mayores que 100 y marcados con estado 'Alto' son: {cuadrado_estado['Alto']}")
print(f"Los cuadrados menores que 100 y marcados con estado 'Bajo' son: {cuadrado_estado['Bajo']}")
#Punto 11 Cuenta cuántos elementos del diccionario anterior fueron clasificados como "alto".
print("\nPunto 11")
print(f"Los cantidad de elementos marcados con estado alto son: {len(cuadrado_estado['Alto'])} ")
#Punto 12 Crea una tupla con los valores del diccionario `cuadrado_estado` clasificados como "bajo" y muéstrala en pantalla.
print("\nPunto 12")
tuplaCuadradoEstado = tuple(cuadrado_estado["Bajo"])
print(f"Los números clasificados como estado 'Bajo' y almacenados en una Tupla son: {tuplaCuadradoEstado}")
#Punto 13 Solicita al usuario un nuevo número. Si ese número ya estaba en la lista `numeros`, indícalo. Si no, agrégalo y actualiza la tupla `referencia`.
print("\nPunto 13")
seguir = True
while seguir:
    numeroNuevo = (input("Ingresa el nuevo número: "))
    esEntero = numeroNuevo.isdigit()
    if esEntero:
        numeroNuevo = int(numeroNuevo)
        if numeros.__contains__(numeroNuevo):
            print(f"El número ingresado ya se encuentra en la lista 'numeros'")
        else:
            numeros.append(numeroNuevo)
            ordenados = sorted(numeros)
            referencia = tuple(ordenados)
            seguir = False
    else:
        print("Ingrese solo números enteros")
print(f"La nueva Tupla ordenada llamada 'Referencia' es así: {referencia}")
#14 Recorre la lista actualizada `numeros` y crea una lista de cadenas que indique por cada valor si es "mayor que el promedio" o "menor o igual al promedio".
print("\nPunto 14")
print(f"El promdio es {promedio:.2f}")
listaMayorPromedio = []
listaMenorPromedio = []
for i in numeros:
    if i > promedio:
        listaMayorPromedio.append(str(i))
    else:
        listaMenorPromedio.append(str(i))
print(f"Mayor que el promedio: {listaMayorPromedio}")
print(f"Menor que el promedio: {listaMenorPromedio}")
#Punto 15 Muestra cuántos valores de `numeros` son distintos de los de la tupla `referencia` (compara posiciones).
print("\nPunto 15")
distintos = 0
for i in range(len(numeros)):
    if numeros[i] != referencia[i]:
        distintos += 1
print(f"La cantidad de números distintos entre la tupla refencia y la lista numeros es: {distintos}")
#Punto 16 Crea un conjunto con las posiciones (índices) en las que el valor de `numeros` es mayor que el de `referencia`.
print("\nPunto 16")
posicionesDistintas = []
for i in range(len(numeros)):
    if numeros[i] > referencia[i]:
        posicionesDistintas.append(i)
print(f"Las posiciones en la lista 'numeros' que son distintas y mayores que en la tupla 'referencia' son: {posicionesDistintas}")
print(f"Lista: {numeros}")
print(f"Tupla: {referencia}")
#Punto 17 Muestra todos los valores de `numeros` que aparecen exactamente una vez, usando solo estructuras básicas.
print("\nPunto 17")
frecuencias = {}
unaVez = []
for i in numeros:
    if i in frecuencias:
        frecuencias[i] += 1
    else:
        frecuencias[i] = 1
for i in frecuencias:
    if frecuencias[i] == 1:
        unaVez.append(i)
masRepetido = (0, 0)
for i in frecuencias:
    if frecuencias[i] > masRepetido[1]:
        masRepetido = (i, frecuencias[i])
print(f"Los números que se repiten una vez son: {unaVez}")
#18 Crea un diccionario `frecuencias` que almacene cuántas veces aparece cada valor en `numeros`. (Solucionado en el punto anterior)
print("\nPunto 18")
print(f"Diccionario con la cantidad de repeticiones: {frecuencias}")
#19 Crea un conjunto con los números que aparecen más de una vez en la lista y que también sean pares.
print("\nPunto 19")
numerosParesConRepeticion = set()
for i in frecuencias:
    if frecuencias[i] > 1 and i % 2 == 0:
        numerosParesConRepeticion.add(i)
print(f"Los números que aparecen más de una vez en la lista y que son pares son: {numerosParesConRepeticion}")
"""20 Muestra un resumen con:
  - Total de números en la lista
  - Cantidad de pares e impares
  - Cantidad de valores "altos" en `cuadrado_estado`
  - Número con mayor frecuencia"""
print("\nPunto 20")
print(f"El total de números de la lista son: {len(numeros)}")
print(f"El total de numeros pares e impares es: Pares={len(clasificacion['Par'])} Impares={len(clasificacion['Impar'])}")
print(f"la cantidad de valores 'Altos' en cuadrado estado son: {len(cuadrado_estado['Alto'])}")
print(f"El número más repetido es: {masRepetido[0]} con {masRepetido[1]} repeticiones")

#numeo de pares e impares y controlar la repeticion de numeros

