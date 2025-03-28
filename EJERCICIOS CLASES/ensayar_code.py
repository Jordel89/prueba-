bañera_capacidad = 500 #litros (límite, se desborda)
bañera_altura = 80 #centimetros
altura_cifón = 70 #centimetros
ritmo_llenado_bañera = 200 #litros por hora

Volumen_persona = 120 # litros volumen
Volumen_bañera_2_horas=200*2

agua_bañera = int(input("Agregar agua a la bañera:"))

while agua_bañera < bañera_capacidad:
    print(f"La bañera no está llena, usted tiene {agua_bañera} litros")

    agua_bañera = agua_bañera + int(input("agregue mas agua:"))

    if agua_bañera > bañera_capacidad:        
        
        Agua_rebosada = agua_bañera - 500        
        print(f"La bañera se llenó con 500 litros, desbordó {int(Agua_rebosada)} litros ")
else:
  print("La bañera está llena con 500 litros")        




    
      