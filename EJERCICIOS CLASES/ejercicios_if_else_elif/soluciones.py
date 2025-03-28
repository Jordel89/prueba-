
# 1. Escribe un programa que pida al usuario un número. Si el número es mayor que 10, imprime "El número es mayor que 10".
numero = float(input("Ingresar un número: "))
if numero>10:
print("El número es mayor que 10")
else:
print("El número es menor que 10")

# 2. Escribe un programa que pida al usuario que ingrese un número. Si el número es positivo, imprime "El número es positivo".
numero = float(input("Ingresar un número: "))
if numero>0:
print("El número es positivo")
elif numero==0:
print("El número es cero. Ni positivo ni negativo")
else:
print("El número es negativo")

# 3. Escribe un programa que pida al usuario que ingrese una contraseña. Si la contraseña es "secreto", imprime "Acceso concedido".
contraseña = input("Ingresar contraseña: ")
if contraseña=="secreto":
print("Acceso concedido")
else:
print("Acceso denegado")

# 4. Escribe un programa que pida al usuario que ingrese dos números. Si el primer número es mayor que el segundo, imprime "El primer número es mayor". De lo contrario, imprime "El segundo número es mayor o igual".
numero1 = float(input("Ingresar un número: "))
numero2 = float(input("Ingresar otro número: "))
if numero1>numero2:
print("El primer número es mayor")
else:
print("El segundo número es mayor o igual")

# 5. Escribe un programa que pida al usuario que ingrese una letra. Si la letra es una vocal, imprime "Es una vocal". De lo contrario, imprime "Es una consonante".
letra = input("Ingresar letra: ")
if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
print("Es una vocal")
else:
print("Es una consonante")

# 6. Ejercicio 1: Escribe un programa que pida al usuario que ingrese un número del 1 al 12. Imprime el nombre del mes correspondiente al número (1: Enero, 2: Febrero, etc.). Si el número no está en el rango del 1 al 12, imprime "Mes inválido".

mes = int(input("Ingresar un número del 1 al 12: "))
if mes==1:
print("Enero")
elif mes==2:
print("Febrero")
elif mes==3:
print("Marzo")
elif mes==4:
print("Abril")
elif mes==5:
print("Mayo")
elif mes==6:
print("Junio")
elif mes==7:
print("Julio")
elif mes==8:
print("Agosto")
elif mes==9:
print("Septiembre")
elif mes==10:
print("Octubre")
elif mes==11:
print("Noviembre")
elif mes==12:
print("Diciembre")
else:
print("Mes invalido")

# 7. Escribe un programa que pida al usuario que ingrese su edad y su género (M o F). Si el usuario es hombre y tiene 65 años o más, o si es mujer y tiene 60 años o más, imprime "Eres elegible para la jubilación". De lo contrario, imprime "No eres elegible para la jubilación".
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su genero: ")

if edad>65 and genero=="M":
print("Eres elegible para la jubilación")
elif edad>60 and genero=="F":
print("Eres elegible para la jubilación")
else:
print("No eres elegible para la jubilación")