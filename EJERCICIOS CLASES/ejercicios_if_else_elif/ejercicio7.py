# 7. Escribe un programa que pida al usuario que ingrese su edad y su género (M o F). 
# Si el usuario es hombre y tiene 65 años o más, o si es mujer y tiene 60 años o más, 
# imprime "Eres elegible para la jubilación".
#  De lo contrario, imprime "No eres elegible para la jubilación".


edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M o F): ").upper()

if (genero == 'M' and edad >= 65) or (genero == 'F' and edad >= 60):
    print("Eres elegible para la jubilación")
else:
    print("No eres elegible para la jubilación")