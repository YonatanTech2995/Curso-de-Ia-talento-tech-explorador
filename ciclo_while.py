"""saldo = 100000
while True:
    opcion =int(input("selecciona una de las 4 opciones: \n1. Consultar saldo \n2. Retirar dinero \n3. Depositar dinero \n4. salir\nSeleccione una opción: "))
    if(opcion == 1):
        print(f"Su saldo actual es {saldo}")
    elif(opcion == 2):
        retirar = int(input("Ingrese el valor a retirar "))
        if(retirar <=0 or retirar >saldo):
            while True:
                retirar = int(input("Ingrese un valor de acuerdo a su saldo actual que no sea inferior a 0 pesos: "))
                if(retirar >0 and retirar <=saldo):
                    break
        saldo = saldo - retirar
        print(f"Su nuevo saldo es {saldo}")
    elif(opcion == 3):
        deposito = int(input("Ingrese el valor a depositar "))
        if(deposito <= 0):
            print("Ingrese un valor superior a 0 pesos ")
        else:
            saldo = saldo + deposito
            print(f"Su nuevo saldo es {saldo}")
    elif (opcion == 4):
        print("Gracias por utilizar nuestroa servicios")
        break
    else:
        print("Ingrese una opción válida")"""

#Ejercicio 2
#participantes: Diego Alegria Yonatan Diaz y Doryey Lame

entradas= 30
salir= False

while True:
    if entradas ==0:
        print("se agotaron las entradas")
        break
    cant_entradas= int(input("¿cuantas entradas deseas comprar?: "))
    if cant_entradas > entradas or cant_entradas <=0:
        print("cantidad no valida")
    elif cant_entradas >0 and cant_entradas <= entradas:
        entradas= entradas - cant_entradas
        print(f"el total a pagar es: {cant_entradas * 8000}")
        while True:
            if entradas==0:
                print("se agotaron las entradas")
                salir=True
                break
            nueva_compra = str(input("¿desea hacer otra compra? (s/n):"))
            if nueva_compra == "s":
                break
            elif nueva_compra != "s" and nueva_compra!= "n":
                print("opcion invalida")
            elif nueva_compra =="n":
                salir = True
                break
        if salir:
            break
    else:
        print("cantidad no valida intente de nuevo")
print("gracias por tu compra")

