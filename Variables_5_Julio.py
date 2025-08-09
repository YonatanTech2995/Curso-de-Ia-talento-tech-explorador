"""#función input
numero =int(input("Ingrese un edad: "))
print("Hola tu edad es", numero)
print("Hola tu edad es 35" + str(numero)) # solo concatena string
print(f"Hola tu edas es {numero}")

#Operadores aritméticos
# suma +
n1 = 5
n2 = 3
suma = n1 + n2
print(f"La suma es: {suma}")
# resta -
n1 = 5
n2 = 3
resta = n1 - n2
print(f"La resta es: {resta}")
# multiplicar *
n1 = 5
n2 = 3
multiplicacion = n1 * n2
print(f"La multiplicacion es: {multiplicacion}")
# modulo %
# potencia **

#operadores Comparación
# diferencia !=
# mayor que >
# menor que <
# mayor o igual que >=
# menor o igual que <=
# igual == para comparación

# Operadores lógicos
# and &
# or |
# not

#Ejercicio 1
numeroPermitido = 1234
numeroIngresado = int(input("Ingrese su número de acceso: "))
edad = int(input("Ingrese su edad: "))
accesoCorrecto = numeroIngresado == numeroPermitido
mayorDeEdad = edad >= 18
print(f"Acceso {accesoCorrecto}")
print(f"Mayor de edad {mayorDeEdad}")
print (f"Estado del acceso {accesoCorrecto and mayorDeEdad}")

#Listas estructura de datos que permite almacenar multiples datos es una sola variable
numeros = [1,5,8,9,5,6,3,6,"Hola","mundo", True, 2.56]
print(numeros[1])
numeros[0] = "yonatan"
print(numeros) 
numeros.append(1995)
print(numeros)
numeros.pop(0)
print(numeros)
numeros.remove(5)
print(numeros)
#len() devuelve el numero de elementos de una lista
longitud = len(numeros)
print(longitud)
palabra = "Yonatan"
print(len(palabra))
numerosOrdenar= [4,8,96,2,78,15,7,8,96,33,25]
numerosOrdenar.sort()
print(numerosOrdenar)

#listas vacias
elementos = []
elementos.append(input(f"Ingrese número 1: "))
elementos.append(input(f"Ingrese número 2: "))
print(f"Lista de elemento: {elementos}")

#Ejercicio 2 Listas
frutas =[]
frutas.append(input(f"Ingresa la primera fruta: "))
frutas.append(input(f"Ingresa la segunda fruta: "))
frutas.append(input(f"Ingresa la tercera fruta: "))
frutas.append(input(f"Ingresa la cuarta fruta: "))
frutas.append(input(f"Ingresa la quinta fruta: "))
print(frutas)
posicion = input("Ingresa el nombre de la primera fruta a eliminar: ")
frutas.remove(posicion)
print(frutas)
posicion =int(input("Ingresa el número de la posición  de la segunda fruta a eliminar: "))
del frutas[posicion - 1]
frutas.sort()
print(frutas)

#Listas tipo Tuplas
numeros = (1,2,3,4,5,6,7,8,9)
print(type(numeros)) #Tuple
diasSemana =("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo")
print(f"El día de la semana es {diasSemana[2]}")
convertirLista = list(diasSemana)
convertirLista.append(11)
print(convertirLista)
nuevaTupla = tuple(convertirLista)
print(nuevaTupla)

#Ejercicio 3 tuplas
productos = (("leche",2500),("queso",4500),("pan",2000), ("galletas",2000),("bocadillo",5000))
listaProductos = list(productos)
nuevoProducto = input("Ingrese el nombre del nuevo elemento: ")
nuevoprecio =int(input("Ingrese el precio del nuevo elemento: "))
listaProductos.append((nuevoProducto,nuevoprecio))
nuevoProducto = input("Ingrese el nombre del nuevo elemento: ")
nuevoprecio =int(input("Ingrese el precio del nuevo elemento: "))
listaProductos.append((nuevoProducto,nuevoprecio))
print(f"Los productos son: {listaProductos[0][0]}, {listaProductos[1][0]}, {listaProductos[2][0]}, { listaProductos[3][0]}, {listaProductos[4][0]}, {listaProductos[5][0]}, {listaProductos[6][0]}")
promedio = listaProductos[0][1] + listaProductos[1][1] + listaProductos[2][1] + listaProductos[3][1] + listaProductos[4][1] + listaProductos[5][1] + listaProductos[6][1]
promedio = promedio / len(listaProductos)
print(f"El promedio de precios es: {promedio:.2f}")
listaProductos.sort(key=lambda x: x[1])
nuevaTupla = tuple(listaProductos)
print(nuevaTupla)

#Ejercicio 4 tuplas 2
listaEstudiantes = []
nombre = input("Ingresa el nombre del alumno 1: ")
edad =int(input("Ingresa la edad del alumno 1: "))
nota =float(input("Ingresa nota final del alumno 1: "))
listaEstudiantes.append((nombre,edad,nota))
nombre = input("Ingresa el nombre del alumno 2: ")
edad =int(input("Ingresa la edad del alumno 2: "))
nota =float(input("Ingresa nota final del alumno 2: "))
listaEstudiantes.append((nombre,edad,nota))
nombre = input("Ingresa el nombre del alumno 3: ")
edad =int(input("Ingresa la edad del alumno 3: "))
nota =float(input("Ingresa nota final del alumno 3: "))
listaEstudiantes.append((nombre,edad,nota))
print(listaEstudiantes)
print(f"Nombres de los estudiantes: {listaEstudiantes[0][0]}, {listaEstudiantes[1][0]}, {listaEstudiantes[2][0]},")
promedio = (listaEstudiantes[0][2] + listaEstudiantes[1][2] + listaEstudiantes[2][2])/ len(listaEstudiantes)
print(f"El promedio general es: {promedio:.2f}")
estudiantesTupla = tuple(listaEstudiantes)
print(estudiantesTupla) """

# Conjuntos no se admiten duplicados
numeros = {0,2,8,9,6,3}
print(type(numeros))
print(numeros)
frutas = {"naranjas","peras", "zanahorias","uvas"}
print(type(frutas))
print(frutas)
frutas.add("lulo")
print(frutas)
frutas.remove("uvas")
print(frutas)
conjuntoUno ={1,2,3,4,5}
conjuntoDos ={4,5,6,7,8,9}
union = conjuntoUno.union(conjuntoDos)
print(union)

