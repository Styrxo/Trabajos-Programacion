import os
import csv
import time

LimpiarCMD = "cls"
opcion = ''

desSalud = ''
desAFP = ''
liqFinal = ' '

try:
    with open("archivo_trabajo.csv", "x") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
except FileExistsError:
    pass

with open("archivo_trabajo.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Trabajador", "Cargo", "Sueldo Bruto", "Desc. Salud", "Desc. AFP", "Líquido a pagar"])

with open("archivo_trabajo.csv", "r", newline="") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)

with open("archivo_trabajo.csv", "r") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    encabezado = next(lector_csv, 0)
    if encabezado != ["Trabajador", "Cargo", "Sueldo Bruto", "Desc. Salud", "Desc. AFP", "Líquido a pagar"]:
        with open("archivo_trabajo.csv", "a") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(["TRABAJADOR", "Cargo", "Sueldo Bruto", "Desc. Salud", "Desc. AFP", "Líquido a pagar"])

with open("archivo_trabajo.csv", "r", newline="") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila[0])

os.system(LimpiarCMD)

elmenu = 1
while elmenu == 1:
    print(" "*10, "MENU", " "*10)
    print("1. Registrar Trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir plantilla de los trabajadores")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        desSalud = 0
        desAFP = 0
        liqFinal = 0
        nombre = input("Ingrese el nombre del trabajador: ")
        if nombre.isdecimal():
            print("Solo se pueden ingresar letras")
            time.sleep(1)
            os.system(LimpiarCMD)
            continue
        elif len(nombre) >= 3:
            print("Nombre ingresado correctamente")
        else:
            print("El nombre debe tener minímo 3 letras.")
            time.sleep(1)
            os.system(LimpiarCMD)
        cargo = input("Ingrese el cargo del trabajor: \n- CEO \n- Desarrollador \n- Analista de datos \n")
        if cargo.isdecimal():
            print("Solo se pueden ingresar letras.")
            time.sleep(1)
            os.system(LimpiarCMD)
            continue
        elif len(cargo) >= 3 and cargo == "CEO" or cargo == "Desarrollador" or "desarrollador" or cargo == "Analista de datos" or "analista de datos":
            print("Cargo ingresado correctamente.")
        else:
            print("Cargo debe tener minimo 3 letras.")
            time.sleep(1)
            os.system(LimpiarCMD)
            continue

        sueldo = int(input("Ingrese el sueldo bruto del trabajor: "))
        if 99999 <= sueldo <= 1000001:
            print("Sueldo ingresado correctamente")
        elif sueldo.isalpha():
            print("Solo se puede ingresar digitos")
        else:
            print("El sueldo debe estar en el rango de 100mil y 1millon.")
        
        desSalud = (sueldo*0.07)
        desAFP = (sueldo*0.12)
        liqFinal = (sueldo-desSalud-desAFP) 

        with open("archivo_trabajo.csv", "a", newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows([
                [nombre, cargo, sueldo, desSalud, desAFP, liqFinal]
                ])
        print("Trabajador ingresado correctamente")
        time.sleep(1)
        os.system(LimpiarCMD)
        continue
        
    elif opcion == 2:
        with open("archivo_trabajo.csv", "r", newline="") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                print(fila[0])

        print("volviendo al menu, el listado no se borrara. \n")
        time.sleep(5)
        continue

    elif opcion == 3:
        with open("archivo_trabajo.csv", "r", newline="") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for i in lector_csv:
                if i:
                    print(", ".join(i))
            
        print("Volviendo al menu, el listado no se borrara. \n")
        time.sleep(5)
        continue

    elif opcion == 4:
        os.system(LimpiarCMD)
        print("Saliendo del programa, muchas gracias.")
        elmenu += 1
        break
            

    else:
        print("Ingrese una opción correcta del menu.")

