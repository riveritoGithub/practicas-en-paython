VALOR_MINIMO = 0
VALOR_MAXIMO = 5

def verificar_rango():
    valor = float(input("Ingresa un valor entre 0 y 5: "))  

    valor_en_rango = VALOR_MINIMO <= valor <= VALOR_MAXIMO

    print(f"Valor dentro de rango: {valor_en_rango}")

verificar_rango()
