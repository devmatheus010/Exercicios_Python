hora1 = int(input("Hora 1: "))
minuto1 = int(input("Minuto 1: "))
if  hora1 > 23  or hora1 <0:
    print("Erro")
    exit()
elif minuto1 > 59 or minuto1 <0:
    print("Erro")
    exit()
elif hora1 > 12:
    hora1 -= 12

hora2 = int(input("Hora 2: "))
minuto2 = int(input("Minuto 2: "))
if  hora2  >23 or hora2  <0:
    print("Erro")
    exit()
elif minuto2 > 59 or minuto2 <0:
    print("Erro")
    exit()
elif hora2 > 12:
    hora2 -=12

horaTotal = hora1 + hora2
if horaTotal > 12:
    horaTotal -= 12
minutoTotal = minuto1 + minuto2
if minutoTotal >= 60:
    minutoTotal -= 60
    horaTotal += 1
if minutoTotal<10:
    print(f"Hora total: {horaTotal}:0{minutoTotal}")
else:
    print(f"Hora total: {horaTotal}:{minutoTotal}")




































