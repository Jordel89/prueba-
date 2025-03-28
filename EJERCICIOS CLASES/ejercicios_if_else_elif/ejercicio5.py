# 5. Escribe un programa que pida al usuario que ingrese una letra. 
# Si la letra es una vocal, imprime "Es una vocal". De lo contrario,
#  imprime "Es una consonante".

letra = input("Ingrese una letra: ").lower()

if letra in ("a","e","i","o","u"):
    print("Es vocal")
else:
    print("Es consonante")
