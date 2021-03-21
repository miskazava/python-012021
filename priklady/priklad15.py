datum_predstaveni = input("Zadej datum představení: ")
pocet_osob = input("Zadej počet vstupenek: ")
pocet_osob = int(pocet_osob)

from datetime import datetime
datum = datetime.strptime(datum_predstaveni, "%d. %m. %Y")
prvni_udalost = datetime(2021, 7, 1)
posledni_udalost = datetime(2021, 8, 31)
if datum < prvni_udalost or datum > posledni_udalost:
  print("Letní kino je v této době uzavřené.")
elif datum < datetime(2021, 8, 11):
  cena = 250 * pocet_osob
  print(f"Celková cena vstupenek je {cena} Kč.")
else:
  cena = 180 * pocet_osob
  print(f"Celková cena vstupenek je {cena} Kč.")
