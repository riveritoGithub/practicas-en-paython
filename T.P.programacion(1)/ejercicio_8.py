def generar_email():
    nombre = "Ricardo Rivero"
    empresa = "IESMB"
    dominio = "com.ar"
    partes_nombre = nombre.split()
    email_usuario = f"{partes_nombre[0].lower()}.{partes_nombre[1].lower()}"  
    email = f"{email_usuario}@{empresa.split()[0].lower()}.{dominio}" 
    print(f"El email generado es: {email}")
generar_email()
