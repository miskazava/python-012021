volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
hodina = input("Zadej hodinu pro rezervaci zasedačky: ")
hodina = int(hodina)
if hodina in volnePokoje:
    print(f"Počet zasedaček k dispozici: {len(volnePokoje[hodina])}")
else:
    print("Zasedačku je možné rezervovat jen v 9, 10, 11 a 12 hod.")