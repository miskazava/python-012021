import math

def overeniCisla(cislo):
    if len(cislo) == 9:
        vysledek = True
    elif len(cislo) == 13:
        if '+420' in cislo:
            vysledek = True
        else:
            vysledek = False
    else:
        vysledek = False
    return vysledek

def cenaZpravy(zprava):
    cena = 3
    delkaZpravy = math.ceil(len(zprava)/180)
    return delkaZpravy * cena

cislo = input("Zadej číslo pro zaslání sms: ")
cislo = cislo.replace(" ", "")
vysledek = overeniCisla(cislo)
if vysledek:
    sms = input("Zadej text zprávy: ")
    cena = cenaZpravy(sms)
    print(f"Cena sms je {cena} Kč.")
else:
    print("Chybny tvar cisla.")