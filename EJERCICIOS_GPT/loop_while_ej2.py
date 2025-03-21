

















#Se establece la suma cero

suma = 0

#pedir numero usuario

numero = int(input("Ingrese un numero(ingrese cero para terminar y sumar):"))

while numero != 0:
    suma = suma + numero
    numero = int(input("Ingrese un numero(ingrese cero para terminar y sumar):"))


print(f"{suma}")  



