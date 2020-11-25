voti1=int(input("Inserire il numero di voti del primo candidato: "))
voti2=int(input("Inserire il numero di voti del secondo candidato: "))
votitot=voti1+voti2
percentuale1=voti1*100
percentuale2=percentuale1/votitot
percentuale3=voti2*100
percentuale4=percentuale3/votitot
if percentuale2>percentuale4:
    print("Ha vinto il primo candidato con una percentuale del",percentuale2,"%")
elif percentuale4>percentuale2:
    print("Ha vinto il secondo candidato con una percentuale del",percentuale4,"%")
else:
    print("Pareggio")
