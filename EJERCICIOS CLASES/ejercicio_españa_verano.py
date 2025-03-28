#En España, las rebajas de invierno suelen comenzar entre los días 1 y 7 de enero y finalizan a final de marzo.
# Por otro lado, las rebajas de verano empiezan durante la primera semana del mes de julio y finalizan durante el mes de septiembre.
#  Para aprovechar la temporada de rebajas de invierno he salido de compras. 
# He pagado 34€ por unos pantalones que tenían un descuento del 15%. 
# ¿Qué precio tenían antes de aplicar el descuento? 
# Si el mismo pantalón cuesta 30€ en la temporada de rebajas de verano y viene con un descuento del 5%,
# es mejor comprarlo en invierno o en verano? compare los precios y retorne True o False.

#¿?

Valor_Real_invierno=34
Valor_Real_Verano=30

Valor_Real_invierno=(Valor_Real_invierno*100)/85

print(Valor_Real_invierno)

Valor_Real_Verano=(Valor_Real_Verano*100)/95

print(Valor_Real_Verano)

print(Valor_Real_Verano<Valor_Real_invierno)

#True:El precio de verano es el mejor
#False: El precio de invierno es mejor