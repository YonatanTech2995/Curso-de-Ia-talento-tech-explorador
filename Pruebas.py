numeros = [5,9,6,2,3,6,8,9,5,6,3,2,5,6,11,45,1]
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
print(f"El número más repetido es: {masRepetido[0]} con {masRepetido[1]} repeticiones")