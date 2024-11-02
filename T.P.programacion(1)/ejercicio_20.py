def clasificacion_a_letra():
    clasificacion = float(input("Ingresa una clasificación numérica (0-10): "))

    if 9 <= clasificacion <= 10:
        letra = 'A'
    elif 8 <= clasificacion < 9:
        letra = 'B'
    elif 7 <= clasificacion < 8:
        letra = 'C'
    elif 6 <= clasificacion < 7:
        letra = 'D'
    elif 0 <= clasificacion < 6:
        letra = 'F'
    else:
        letra = "Desconocido"

    print(f"La clasificación en letra es: {letra}")

clasificacion_a_letra()
