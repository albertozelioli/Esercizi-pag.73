print("Calcolatore dei veicoli transitati in un determinato periodo di tempo ")
auto = []
while True:
    transito = int(input("Inserire il numero di auto transitate oggi: "))
    if transito == 0:
        break
    else:
        auto.append(transito)
autosum = sum(auto)
print("Il totale delle auto che hanno transito è ", autosum)
