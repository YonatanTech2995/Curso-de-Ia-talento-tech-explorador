"""Grupo 1: Debe crear una función llamada registrar_productos() que:

Pida al usuario cuántos productos va a registrar.

Para cada producto, solicite nombre y precio unitario.

Devuelva un diccionario donde la clave sea el nombre y el valor sea el precio."""

def registrar_productos():
    productos = {}
    try:
        while True:
            cantidad = int(input("¿Cuántos productos va a registrar? "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
            else:
                for i in range(cantidad):
                    nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
                    while True:
                        try:
                            precio = float(input(f"Ingrese el precio unitario de {nombre}: "))
                            if precio < 0:
                                print("El precio no puede ser negativo. Intente nuevamente.")
                            else:
                                break
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número válido para el precio.")
                    productos[nombre] = precio
            if len(productos) == cantidad:
                break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido para la cantidad de productos.")
    return productos
productod_finales = registrar_productos()
print("Productos registrados:", productod_finales)