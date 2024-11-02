def calcular_costo_envio():
    destino = input("Ingresa el destino (nacional o internacional): ").strip().lower()
    
    peso = float(input("Ingresa el peso del paquete en kilogramos: "))

    costo = 0

    if destino == "nacional":
        costo = 10 * peso  
    elif destino == "internacional":
        costo = 20 * peso  
    else:
        print("Destino desconocido. Por favor, ingresa 'nacional' o 'internacional'.")

    if costo > 0:
        print(f"El costo de envío del paquete es: ${costo:.2f}")

 
calcular_costo_envio()
