"""contactos = {
    "Juan" : 12345,
    "Maria" : 56989,
    "Yonatan" : 894646,
} #Las claves no se pueden duplicar que es el que esta antes de los dos puntos
print(type(contactos))
print(contactos)
#print(elefonoMaria = contactos["Maria"])
print(contactos["Maria"])
numeroJuan = contactos["Juan"]
print(numeroJuan)

#Métodos más comunes en diccionarios
#Metodo keys(): devuelve las claves de un diccionario
llaves = contactos.keys()
print(llaves)
#Método values(): devuelve los valores de un 
Valores = contactos.values()
print(Valores)
#Método Items
clavevalores = contactos.items()
print(clavevalores)
#Agregar
contactos["Angelita"] = 55689
print(contactos)
#Modificar
contactos["Yonatan"] = 1995
print(contactos)
#Eliminar
contactos.pop("Yonatan")
print(contactos)
del contactos["Juan"]
print(contactos)"""

"""Ejercicio 1
Crear un sistema de tienda recibe por teclado la siguiente información de tres productos (uno a uno):

Nombre del producto

Categoría del producto

Precio del producto

Luego de ingresar estos datos, realiza lo siguiente:

Guarda cada producto como una tupla con los datos. listo

Agrupa las 3 tuplas en una lista llamada productos. listo

Crea un conjunto con las categorías únicas. listo

Construye un diccionario donde cada clave sea el nombre del producto y el valor sea su precio. listo

Imprime la lista de productos, el conjunto de categorías y el diccionario de precios. listo

productos = []
nombreProducto = input(f"Ingrese el nombre del primer producto: ")
categoriaProducto = input(f"Ingrese la categoría del primer producto: ")
precioProducto = input(f"Ingrese el precio del primer producto: ")
producto1 = (nombreProducto,categoriaProducto,precioProducto)
nombreProducto2 = input(f"Ingrese el nombre del segundo producto: ")
categoriaProducto2 = input(f"Ingrese la categoría del segundo producto: ")
precioProducto2 = input(f"Ingrese el precio del segundo producto: ")
producto2 = (nombreProducto2,categoriaProducto2,precioProducto2)
nombreProducto3 = input(f"Ingrese el nombre del tercer producto: ")
categoriaProducto3 = input(f"Ingrese la categoría del tercer producto: ")
precioProducto3 = input(f"Ingrese el precio del tercer producto: ")
producto3 = (nombreProducto3,categoriaProducto3,precioProducto3)
productos = [producto1, producto2, producto3]
tuplaProductos = tuple(productos)
categorias = {productos[0][1],productos[1][1],productos[2][1]}
diccionarioProductos = {
    productos[0][0]: productos[0][2],
    productos[1][0]: productos[1][2],
    productos[2][0]: productos[2][2],
}
print(f"Se esta imprimiendo la lista de productos: {productos}")#lista
print(f"Se esta imprimiendo las categorías de los productos: {categorias}")#Categorías
print(f"Se esta imprimiendo el diccionario de los productos: {diccionarioProductos}")#diccionario

#Condicionales if, elif, else
edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print("Eres un niño")
elif edad <= 17 and edad >11:
    print("Eres adolecente")
elif edad <60 and edad >17:
    print("Eres adulto")
else:
    print("Eres adulto mayor")"""

"""#Un estudiante presenta 3 evaluaciones con los siguientes porcentajes: parcial 1: 30%, parcial 2: 30% y parcial 3: 40%, con nota menor a 3 reprobado, con no ta de 3 a 3.9 semiaprovado, de 4 a 4.5 aprobado y de 4.6 a 5 aprobado con honores
nombreEstudiante = input("Ingresa el nombre del estudiante: ")
if nombreEstudiante.replace(" ","").isalpha():
    print("Es texto")
    notaUno = float(input("Ingrese primera nota: "))
    notaDos = float(input("Ingrese segunda nota: "))
    notaTres= float(input("Ingrese segunda nota: "))
    if 0<= notaUno <= 5 and 0<= notaDos <= 5 and 0<= notaTres <= 5:
        Promedio = ((notaUno * 0.3)+ (notaDos*0.3) + (notaTres*0.4)).__round__(1)
        print(Promedio)
        if Promedio < 3:
            print(f"El estudiante {nombreEstudiante} obtuvo una nota de {Promedio} por ende su estado es Reprobado")
        elif Promedio <= 3.9:
            print(f"El estudiante {nombreEstudiante} obtuvo una nota de {Promedio} por ende su estado es Semiaprobado")
        elif Promedio <= 4.5:
            print(f"El estudiante {nombreEstudiante} obtuvo una nota de {Promedio} por ende su estado es Aprobado")
        else: print(f"El estudiante {nombreEstudiante} obtuvo una nota de {Promedio} por ende su estado es Aprobado con honores")
    else: print("Ingrese datos válidos")
else: print ("No es texto")"""

#Ejercicio 2 
nombre = input("Nombre: ")
edad = int(input("Edad: "))
if edad<=0:
    print("La edad ingresada no es válida")
    exit()
valorCompra = float(input("Valor de la compra: "))
if edad >=18:
    tarjeta = input("¿Tiene tarjeta del cliente fiel? (si/no): ").lower()
    diaEspecial = input("¿Es día especial de promoción? (si/no): ").lower()
descuento = 0
if edad < 18:
    descuento = 0
elif 18 <= edad <= 60:
    if tarjeta == "si" and diaEspecial == "si":
        descuento = 0.20
    elif tarjeta == "si":
        descuento = 0.10
    elif diaEspecial == "si":
        descuento = 0.05
    else:
        descuento = 0
elif edad > 60:
    descuento = 0.15
    if tarjeta == "si":
        descuento = 0.25
valor_descuento = valorCompra * descuento
total_pagar = valorCompra - valor_descuento
print("\n--- Resumen de compra ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Valor de la compra: ${valorCompra}")
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Total a pagar: ${total_pagar}")