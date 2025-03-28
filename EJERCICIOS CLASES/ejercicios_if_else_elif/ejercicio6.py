# 6. Escribe un programa que pida al usuario que ingrese un número del 1 al 12. 
# Imprime el nombre del mes correspondiente al número (1: Enero, 2: Febrero, etc.). 
# Si el número no está en el rango del 1 al 12, imprime "Mes inválido".

numero = int(input("Escriba un número del 1 - 12: "))

if numero == 1:
    print("1: Enero")
elif numero == 2:
    print("2: Febrero")
elif numero == 3:
    print("3: Marzo")
elif numero == 4:
    print("4: Abril")
elif numero == 5:
    print("5: Mayo")
elif numero == 6:
    print("6: Junio")
elif numero == 7:
    print("7: Julio")
elif numero == 8:
    print("8: Agosto")
elif numero == 9:
    print("9: Septiempbre")
elif numero == 10:
    print("10: Octubre")
elif numero == 11:
    print("11: Noviembre")
elif numero == 12:
    print("12: Diciembre")
else:
    print("Mes inválido.")

