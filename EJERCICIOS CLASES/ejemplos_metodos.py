import re

saludo = "hola a todos, cómo están"

# Usamos re.split() para dividir por 'o' y 'ó'
resultado = re.split('[oóaá]', saludo)

print(resultado)  # Esto imprimirá ['h', 'la a t', 'd', 's, c', 'm', ' est', 'n']
