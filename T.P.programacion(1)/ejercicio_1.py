
def presentarse():
    
    nombre = input("¿Cuál es tu nombre? ")
    

    while True:
        try:
            edad = int(input("¿Cuál es tu edad? "))  
            break  
        except ValueError:
            print("Por favor, ingresa un número entero válido para la edad.") 
    
    
    pais = input("¿Cuál es tu país? ")
    
   
    print(f"Hola, mi nombre es {nombre}, tengo {edad} años y soy de {pais}.")


presentarse()
