def generar_id_unico():
    nombre = input("¿Cuál es tu nombre? ")
    apellido = input("¿Cuál es tu apellido? ")
    año_nacimiento = input("¿Cuál es tu año de nacimiento? ")
    id_unico = f"{nombre[0].lower()}{apellido[0].lower()}{año_nacimiento}"
    print(f"Tu ID único es: {id_unico}")
generar_id_unico()