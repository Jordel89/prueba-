# Pedimos numero positivo
numero = int(input("Escribe un número positivo:"))

# Verificamos si es numero positivo
while numero <= 0:
    print("por favor, ingresa un número positivo.")
    numero = int(input("escriba un número positivo:"))

# Usamos loop while para imprimir los numeros desde el numero hasta 1
while numero >= 1:
    print(numero)
    numero -= 2 # decrementamos el numero en 1 en cada iteración

    