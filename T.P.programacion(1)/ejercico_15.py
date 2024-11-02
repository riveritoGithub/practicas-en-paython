def calcular_rectangulo():
    base = float(input("Ingresa la base del rectángulo: "))
    
    altura = float(input("Ingresa la altura del rectángulo: "))

    area = base * altura

    perimetro = 2 * (base + altura)

    print(f"Área del rectángulo: {area}")
    print(f"Perímetro del rectángulo: {perimetro}")

calcular_rectangulo()
