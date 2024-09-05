time1 = input("Nome do time 1:  ")
time2 = input("Nome do time 2: ")
golTime1 = int(input(f"Quantos gols o time do {time1} fez: "))
golTime2 = int(input(f"Quantos gols o time do {time2} fez: "))

if golTime1 > golTime2:
    print(f"{time1} {golTime1} vs {golTime2} {time2}. Vitoria do {time1} \n")
elif golTime2 > golTime1:
    print(f"{time2} {golTime2} vs {golTime1} {time1}. Vitoria do {time2}\n")
else:
    print(f"{time1} {golTime1} vs {golTime2} {time2}. O jogo terminou empatado")
