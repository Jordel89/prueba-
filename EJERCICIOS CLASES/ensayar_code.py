bañera_capacidad = 500 #litros (límite, se desborda)
bañera_altura = 80 #centimetros
altura_cifón = 70 #centimetros
ritmo_llenado_bañera = 200 #litros por hora

Volumen_persona = 120 # litros volumen
Volumen_bañera_2_horas=200*2

agua_bañera = int(input("Agregar agua a la bañera:"))

while bañera_capacidad > 499:
    print("la bañera no está llena!")
    agua_bañera = int(input(f"Agregar más agua a la bañera, usted tiene {input} litros"))
if bañera_capacidad == 500:
  print(f"Bañera llena, con {str(bañera_capacidad)} litros")
else :
   print(f"bañera desbordada, con {str(agua_bañera)} - {str(bañera_capacidad)}")
  
    
      