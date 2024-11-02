def calcular_descuento():
    monto = float(input("Ingresa el monto de la compra: "))
    
    es_miembro = input("¿Eres miembro de la tienda? (sí/no): ").strip().lower()

    descuento = 0

    if monto > 1000 and es_miembro == "sí":
        descuento = 0.10  
    elif es_miembro == "sí":
        descuento = 0.05  
    else:
        descuento = 0.0   

    monto_descuento = monto * (1 - descuento)

    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Monto total después del descuento: ${monto_descuento:.2f}")

calcular_descuento()
