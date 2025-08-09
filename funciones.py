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

variosParametros("hola","mundo", 9, " de agosto") 