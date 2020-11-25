candidato1 = input("Inserire il nome del primo candidato? ")
voti1 = int(input("Inserire il numero di voti del primo candidato? "))
candidato2 = input("Inserire il nome del secondo candidato? ")
voti2 = int(input("Inserire il numero di voti del secondo candidato? "))
candidati = [candidato1, candidato2]
candidati.sort()
print("L'elenco dei candidati in ordine alfabetico è:",candidati)
elencovoti = [voti1, voti2]
elencovoti.reverse()
print("L'elenco dei punteggi in ordine decrescente è:",elencovoti)
print("Mentre l'elenco dei candidati in ordine decrescente di punteggi è:")
if voti1 < voti2:
    print(candidato2, candidato1)
elif voti2 < voti1:
    print(candidato1, candidato2)
