horas = int(input("Digite la hora de inicio (horas de 0 a 23): "))

minutos= int(input("Digite los minutosinicio (minutos de 0 a 59): "))

duracion = int(input("Duración del evento en minutos(minutos): "))

minutos = minutos + duracion

horas = horas + minutos // 60

minutos = minutos % 60

horas = horas % 24

print('el evento terminará a las:')

print(horas, ":", minutos)