def reservar_hotel():
    nombre_cliente = input("Ingresa tu nombre: ")

    dias_estadia = int(input("¿Cuántos días te quedarás en el hotel? "))

    vista_al_mar = input("¿Deseas un cuarto con vistas al mar? (sí/no): ").strip().lower()

    tarifa_sin_vista = 10000  
    tarifa_con_vista = 15000   

    if vista_al_mar == "sí":
        costo_total = tarifa_con_vista * dias_estadia
        tipo_cuarto = "con vistas al mar"
    else:
        costo_total = tarifa_sin_vista * dias_estadia
        tipo_cuarto = "sin vistas al mar"

    print(f"\nReservación para: {nombre_cliente}")
    print(f"Días de estadía: {dias_estadia}")
    print(f"Tipo de cuarto: {tipo_cuarto}")
    print(f"Costo total de la estadía: ${costo_total}")

reservar_hotel()
