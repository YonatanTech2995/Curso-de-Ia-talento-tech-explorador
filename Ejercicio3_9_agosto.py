#punto 1 Registrar estudiantes y sus 3 notas usando try except
def registrar_estudiantes():
    estudiantes = {}
    ingresarEstudiantes = True
    estudiante = 1
    contador = 0
    while ingresarEstudiantes: 
        nombre = input(f"Ingrese el nombre del estudiante {estudiante}(o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            notas = []
            for i in range(3):
                while True:
                    nota = float(input(f"Ingrese la nota {i + 1} de {nombre}: "))
                    if nota < 0 or nota > 5:
                        print("La nota debe estar entre 0 y 5.")
                    else:
                        notas.append(nota)
                        break
            estudiantes[nombre] = notas
            contador += 1
            estudiante += 1
            if contador == 3:
                ingresarEstudiantes = False
        except ValueError:
            print(f"Error: {ValueError}. Intente nuevamente.")
    return estudiantes

#punto 2 Calcular el promedio de cada estudiante.
def calcular_promedios(estudiantes):
    promedios = {}
    for nombre, notas in estudiantes.items():
        if len(notas) == 3:
            promedio = sum(notas) / 3
            promedios[nombre] = promedio
        else:
            print(f"El estudiante {nombre} no tiene 3 notas registradas.")
    return promedios