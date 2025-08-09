#Finciones
#Evitan repetir código
#Reutilizar procesos comunes
#Organiza mejor el código
#Facil para leer y entender el código


#TIPOS DE FINCIONES 
#Funcion sin parametros y sin retorno
def mostarMensaje():
    print("Hola mundo")

#funcion con parametro y sin retorno
def mostrarMensaje2(nombre):
    print(f"hola {nombre}")

def mostrarMensaje3(nombre, apellido = "Diaz"): #El = se usa para dar un valor si el parametro no es enviado, solo funciona si el parametro esta despues de argumentos no predeterminados.
    print(f"hola {nombre} {apellido}")

#funciones sin parametros y con retorno
def obtener_pi():
    return 3.1416

def suma(a, b, c = 5): # tambien aplica para agumentos predeterminados ejm_ c = 5
    return a + b + c

#funcion con varios parametros sin saber cuantos parametros se van a recibir 
def variosParametros(*numeros_letras): # se agrega un * al inicio del parametro
    print(numeros_letras)

def sumar(*numeros):
    return sum(numeros)
#Funciones lamba
sumar_lambda = lambda a, b: a + b
multiplicar_lambda = lambda a, b: a * b

#función map
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
doblados = list(map(lambda x: x * 2, numeros))  # Multiplica cada elemento de la lista por 2
print(doblados)

#función filter
pares = list(filter(lambda x: x % 2 == 0, numeros))# Filtra los números pares de la lista
print(pares)

#función sorted
nombres = ["Juan", "Ana", "Pedro", "Maria", "jorge", "luis", "carlos", "maria", "laura", "jose", "carmen"]
nombres_ordenados = sorted(nombres, key=lambda x: len(x))  # Ordena los nombres sin importar mayúsculas o minúsculas
print(nombres_ordenados)