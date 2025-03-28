# 4. Escribe un programa que pida al usuario que ingrese dos números. 
# Si el primer número es mayor que el segundo, imprime "El primer número es mayor".
#  De lo contrario, imprime "El segundo número es mayor o igual".

primer_numero = int(input("Ingrese un número: ")) 
segundo_numero = int(input("Ingrese otro número: "))

if primer_numero > segundo_numero:
    print(f"El primer número es mayor.")
else:
    print("el segundo número es mayor o igual")