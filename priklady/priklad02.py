sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod = input("Zadej kód součástky: ")
if kod in sklad:
    mnozstvi = input("Zadej požadované množství: ")
    if int(sklad[kod]) < int(mnozstvi):
        print(f"Požadované množství není skladem. Max. množství je {str(sklad[kod])} ks.")
        sklad.pop(kod)
        print(sklad)
    else:
        print("Požadované množství je skladem. Objednávka bude úspěšně dokončena.")
        sklad[kod] = int(sklad[kod]) - int(mnozstvi)
        if sklad[kod] == 0:
            sklad.pop(kod)
            print(sklad)
        else:
            print(sklad)
else:
    print("Součástka není skladem.")