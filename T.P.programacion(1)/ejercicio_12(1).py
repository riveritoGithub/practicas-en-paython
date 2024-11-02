import random

def generar_id_unico():
    nombre = input("¿Cuál es tu nombre? ")
    apellido = input("¿Cuál es tu apellido? ")
    año_nacimiento = input("¿Cuál es tu año de nacimiento (YYYY)? ")
    letras_nombre = nombre[:2].upper()
    letras_apellido = apellido[:2].upper()
    ultimos_digitos_año = año_nacimiento[-2:] 
    valor_aleatorio = random.randint(1000, 9999)
    id_unico = f"{letras_nombre}{letras_apellido}{ultimos_digitos_año}{valor_aleatorio}"
    print(f"Tu ID único es: {id_unico}")
generar_id_unico()
