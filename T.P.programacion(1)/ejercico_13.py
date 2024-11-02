USUARIO_CORRECTO = "usuario123"
PASSWORD_CORRECTO = "contraseña456"

def validar_usuario_password():
    usuario = input("Ingresa tu usuario: ")
    
    password = input("Ingresa tu contraseña: ")

    es_valido = (usuario == USUARIO_CORRECTO) and (password == PASSWORD_CORRECTO)

    print(es_valido)

validar_usuario_password()
