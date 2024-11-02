USUARIO_VALIDO = "admin"
PASSWORD_VALIDO = "1234"

def validar_usuario_password():
    usuario = input("Ingresa tu usuario: ").strip()
    
    password = input("Ingresa tu password: ").strip()

    if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
        print("Bienvenido al sistema")
    elif usuario != USUARIO_VALIDO and password == PASSWORD_VALIDO:
        print("Usuario inválido")
    elif usuario == USUARIO_VALIDO and password != PASSWORD_VALIDO:
        print("Password inválido")
    else:
        print("Usuario y password inválidos")
validar_usuario_password()
