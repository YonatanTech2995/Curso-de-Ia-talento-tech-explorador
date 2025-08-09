print("Encuesta servicios públicos")
votos = [0, 0, 0, 0]
categorias = ["Malo", "Regular", "Bueno", "Excelente"]

encuestas = 0

while encuestas < 4:

    print("¿Cómo califica el servicio recibido?")
    print("1. Malo")
    print("2. Regular")
    print("3. Bueno")
    print("4. Excelente")

    respuesta = input("Ingrese una opción: ")

    if respuesta.isdigit():
        respuesta = int(respuesta)

        if 1 <= respuesta <= 4:
            votos[respuesta - 1] += 1
            encuestas += 1

            respuesta_continuar = ""
            while respuesta_continuar != 's' and respuesta_continuar != 'n' and respuesta_continuar != 'S' and respuesta_continuar != 'N':
                respuesta_continuar = input("¿Registrar una nueva respuesta? (s/n): ")

                if respuesta_continuar == 's' or respuesta_continuar == 'S':
                    print("Siguiente encuesta.")
                elif respuesta_continuar == 'n' or respuesta_continuar == 'N':
                    encuestas = 4  # finaliza la encuesta
                else:
                    print("Respuesta no válida. Debe escribir 's' o 'n'.")
        else:
            print("Opción no válida. Solo se permiten números del 1 al 4.")
    else:
        print("Entrada no válida. Debe ingresar un número del 1 al 4.")

# Mostrar el resumen final
print("-- Resumen de la encuesta ---")
print(f"Total de encuestas realizadas: {sum(votos)}")

indice = 0
while indice < len(categorias):
    print(f"{categorias[indice]}: {votos[indice]} voto(s)")
    indice += 1