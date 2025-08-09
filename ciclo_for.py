"""#imprimir numero del 1 al 10
for i in range(1,11):
    print(i)

#imprimir frutas
frutas = ["Naranjas","Peras","Bananos","mangos"]
for i in frutas:
    print(i)

#Numeros pares en un lista
numeros = [9,56,78,12,59,63,1,2,73,98]
con = 0
for i in numeros:
    if i % 2 == 0:
        con+=1
print(con)

#Sumar numeros de una lista
lista = [8,4,5,9,6,3,2,5,9,8,7,8,4,5,56,8,9]
suma = 0
for i in lista:
    suma = i + suma
print(suma)"""

#Ejercicio 1
"""notas = [4.5, 2.8, 3.9, 1.7, 5.0, 3.0, 2.5, 4.2, 1.8, 3.3]
print (len(notas))

print("Notas de los estudiantes:") #Imprime todas las notas
for i in notas:
    print(i, end=", ")
print()
suma = 0 #Calcular promedio
for i in notas:
    suma = i + suma
promedio = suma / len(notas)
print(f"El promedio general es: {promedio :.2f}")

contador = 0 #numero de estudiantes por encima de 3.0
for i in notas:
    if i >= 3.0:
        contador += 1
print(f"El número de estudiantes aprobado es {contador}")
print(f"El número de estudiantes que reprobaron es {len(notas) - contador}")

listaAprobados = []
for i in notas:
    if i >= 3.0:
        listaAprobados.append(i)
print(f"La lista de notas aprobadas es: {listaAprobados}")

notaMasAlta = promedio #Nota mas lata y mas baja
notaMasBaja = promedio
for i in notas:
    if i > notaMasAlta:
        notaMasAlta = i
    elif i < notaMasBaja:
        notaMasBaja = i
print(f"La nota más alta registrada es: {notaMasAlta}")
print(f"La nota más baja registrada es: {notaMasBaja}")"""

#Con cadena de caracteres
"""palabra = "Hola mundo"
for i in palabra:
    print(i,end="")

#for tipo range
for i in range(1,101):
    print(i, end=" ")
for i in range(1,100,2):
    print(i, end=" ")

for i in range(1,6):
    for n in i:
        print("*")

#Ejercicio 2
animales = {"perro": 4, "Pez": 0, "pájaro": 2, "gato": 4}
listaP = []
for i in animales:
    animal = i
    i = i.lower()
    if i.startswith("p"):
        listaP.append(animal)
print(f"La lista de animales que comienza por p es: {listaP}")

#Ejercicio 3
edades = {"Ana": 18, "Luis": 22, "Carlos": 30}
buscar = True
encontrado = False
while buscar:
    nombre = input("Ingresa un nombre o digita salir: ")
    if nombre.lower() == "salir":
        buscar = False
        break
    for i in edades:
        if i == nombre:
            print(f"{nombre} tiene {edades[i]} años.")
            break
    if not encontrado:
        print("Ese nombre no está en el diccionario.")"""

#Ejercicio 4
letras = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,"l": 12,"m": 13,"n": 14,"o": 15,"p": 16,"q": 17,"r": 18,"s": 19, "t": 20,"u": 21,"v": 22,"w": 23,"x": 24,"y": 25,"z": 26,}
seguir = True
while seguir:
    palabra = input("Ingrese el nombre de la fruta sin tildes: ").lower()
    contiene = False
    palabra = palabra.replace(" ","")
    if palabra == "salir":
        seguir = False
        break
    tildes = ["á","é","í,","ó","ú"]
    for i in tildes:
        if palabra.__contains__(i):
            print("La palabra contiene tildes")
            contiene = True
    if not contiene:
        listaFruta = []
        codigoFinal = []
        for i in palabra:
            valorLetra = letras[i]
            listaFruta.append(valorLetra)
        for i in listaFruta:
            contador = 0
            for n in listaFruta:
                if i == n:
                    contador += 1
            valorLetra = i * contador
            codigoFinal.append(valorLetra)
        print(codigoFinal)
