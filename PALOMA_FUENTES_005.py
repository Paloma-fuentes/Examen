import random
import os
import csv
import math
print("Bienvenido al programa calculador de promedio de sueldos")

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

print("Eliga la opcion que desea ejecutar:\n ")
print("1. Asignar sueldos\n 2.Caificar sueldos\n 3. Ver estadisticas\n 4. Reporte de sueldos\n 5. Salir del programa")
sueldo = []

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Los sueldos fueron asignados correctamente.\n ")

def calificar_sueldos():
    menores = []
    medios = []
    mayores = []
    for i, sueldo in enumerate(sueldo):
        if sueldo < 800000:
            menores.append((trabajadores[i], sueldo))
        elif 800000 <= sueldo <= 2000000:
            medios.append((trabajadores[i], sueldo))
        else: 
            mayores.append((trabajadores[i], sueldo))
    
    print("Sueldos menores a $800.000 total: ", len(medios))
    for nombre, sueldo in menores:
        print(f"{nombre} {sueldo}")

    print("Sueldos entre $800.000 y $2.000.000 total: ", len(medios))
    for nombre, sueldo in medios:
        print(f"{nombre} {sueldo}")
    
    print("Sueldos superiores a $2.000.000 total: ", len(mayores))
    for nombre, sueldo in mayores:
        print(f"{nombre} {sueldo}")

    print("\nTOTAL SUELDOS: $", sum(sueldos), "\n")

def ver_estadisticas():
    if not sueldos:
        print("Debe asignar sueldos a los trabajadores")
        return
    
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos)/ len(sueldos)
    medida_geo = math.exp(sum(math.log(s) for s in sueldos) / len(sueldos))

    print(f"El sueldo mas alto es: $ {sueldo_max}")
    print(f"El sueldo menor es: $ {sueldo_min}")
    print(f"El promedio de sueldos es el siguiente: $ {sueldo_promedio: .2f}")
    print(f"La medida geometrica de los sueldos es: $ {medida_geo: .2f}\n")

def reporte_sueldos():
    if not sueldos:
        print("Primero debe asignar sueldos a cada trabajador:\n ")
        return
    
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        fieldnames = ["Nombre trabajador", "Sueldo base", "Descuento salud", "Descuento AFP", "Sueldo liquido"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()

        for i, sueldo in enumerate(sueldos):
            descuento_salud = sueldo * 0.70
            descuento_AFP = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_AFP
            writer.writerow({
                "Nombre trabajador " : trabajadores[i],
                "Sueldo base" : sueldo,
                "Descuento Salud" : descuento_salud,
                "Descuento AFP" : descuento_AFP,
                "Sueldo liquido" : sueldo_liquido
            })

print("El reporte de sueldos a sido creada exitosamente.\n")

def main():
    while True:
        print("Eliga la opcion que desea ejecutar:\n ")
        print("1. Asignar sueldos\n 2.Caificar sueldos\n 3. Ver estadisticas\n 4. Reporte de sueldos\n 5. Salir del programa")

        opcion = input("Ingrese el numero de la opcion: ")

        if opcion == "1":
            asignar_sueldos_aleatorios()
        elif opcion == "2":
            calificar_sueldos()
        elif opcion =="3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Finalizando el programa")
            print("Desarrollado por Paloma Fuentes")
            print("RUT 20.814.882-6")
        else:
            break

main()
        



