def mayor_de_dos_numeros():
    numero1 = int(input("Ingresa el primer número entero: "))
    
    numero2 = int(input("Ingresa el segundo número entero: "))

    if numero1 > numero2:
        mayor = numero1
    elif numero2 > numero1:
        mayor = numero2
    else:
        mayor = None  

    if mayor is not None:
        print(f"El número mayor es: {mayor}")
    else:
        print("Ambos números son iguales.")

mayor_de_dos_numeros()
