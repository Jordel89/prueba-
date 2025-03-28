#condicional if-else-elif. Sirve para poner mas condiciones después del if, se sierra con un else.  
print("--- Condicional if-else_elif ____n")

nota = 100

if nota >= 90:
    print("Exelente")
elif nota >= 70:
    print("muy bien")
elif nota >= 50:
    print("aceptable")
else:
    print("puedes mejorar")

#elif permite evaluar multiples condicionales.
#se ejecuta el bloque de código del primer elif cuya condición sea verdadera.
# si ninguna condición es verdadera, se ejecuta el código del código else.
