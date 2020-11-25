print("Calcolatore media stipendi dei dipendenti dell'azienda")
stipendi = []
while True:
    stipendio = int(input("Inserire lo stipendio: "))
    if stipendio == -1:
        break
    else:
        stipendi.append(stipendio)
stipenditot = len(stipendi)
stipendisum = sum(stipendi)
media = stipendisum/stipenditot
print("La media degli stipendi dei dipendenti è di ", media, "€")
