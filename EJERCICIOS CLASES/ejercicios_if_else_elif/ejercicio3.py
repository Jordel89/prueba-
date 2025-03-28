# 3. Escribe un programa que pida al usuario que ingrese una contraseña. 
# Si la contraseña es "secreto", imprime "Acceso concedido".

contraseña_usuario = str(input("Escriba su contrseña: "))

if contraseña_usuario == "secreto":
    print("Acceso concedido")
else:
    print("Acceso denegado")