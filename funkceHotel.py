def totalPrice(persons, breakfast=False):
    cena = nightPrice
    if breakfast:
        cena += breakfastPrice
    return cena*persons
nightPrice = 850
breakfastPrice = 125
celkovaCena = totalPrice(2, True)
print(f"Cena za jednu noc v hotelu je {celkovaCena} Kc.")
celkovaCena = totalPrice(3)
print(f"Cena za jednu noc v hotelu je {celkovaCena} Kc.")
