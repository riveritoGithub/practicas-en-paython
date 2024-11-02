nombre = input("ingrese su nombre:")
dias_de_estadia = int(input("¿cuntos dia se quedara en el hotel?:"))
tarifa_dia = float(input("¿cual es la tarifa por dia(en moneda local)?:"))
costo_total = dias_de_estadia * tarifa_dia
print("\nreserva realizada con exito:")
print(f"Nombre:{nombre}")
print(f"usted estara un total de :{dias_de_estadia}")
print(f"costo total de la estadia :{costo_total}")

