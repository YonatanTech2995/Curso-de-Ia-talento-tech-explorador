#Punto 3 Mostrar un ranking del mejor al peor promedio.
from Ejercicio3_9_agosto import *
def main():
    estudiantes = registrar_estudiantes()
    print(estudiantes)
    promedios = calcular_promedios(estudiantes)
    mostrar_ranking(promedios)

def mostrar_ranking(promedios):
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    print("\nRanking de estudiantes por promedio:")
    for i, (nombre, promedio) in enumerate(ranking, start=1):
        print(f"{i}. {nombre}: {promedio:.2f}")
main()


