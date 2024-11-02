def determinar_estacion():
    mes = int(input("Ingresa el número del mes (1-12): "))

    if mes in [1, 2, 12]:
        estacion = "Invierno"
    elif mes in [3, 4, 5]:
        estacion = "Primavera"
    elif mes in [6, 7, 8]:
        estacion = "Verano"
    elif mes in [9, 10, 11]:
        estacion = "Otoño"
    else:
        estacion = "Desconocido"

    print(f"La estación del año es: {estacion}")

determinar_estacion()
