class Auto:

    def __init__(self, registracniZnacka, znacka, typVozidla, pocetKilometru):
        self.registracniZnacka = registracniZnacka
        self.znacka = znacka
        self.typVozidla = typVozidla
        self.pocetKilometru = pocetKilometru
        self.volne = True

    def pujc_auto(self):
        if self.volne == False:
            return "Vozidlo není k dispozici."
        else:
            self.volne = False
            return "Potvrzuji zapůjčení vozidla."

    def get_info(self):
        return f"{self.registracniZnacka}, {self.znacka}, {self.typVozidla}"

    def vrat_auto(self, tachometr, pocetDni):
        self.tachometr = tachometr
        self.volne = True
        pocetDni = int(pocetDni)
        if pocetDni > 7:
            cena = 300 * pocetDni
        else:
            cena = 400 * pocetDni
        return cena

auto1 = Auto("4A2 3020", "Peugeot", "403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda", "Octavia", 41253)

znacka = input("Zadej značku auta, o kterou máš zájem (Peugeot/Škoda): ")
if znacka == "Peugeot":
    auto = auto1
if znacka == "Škoda":
    auto = auto2
print(auto.get_info())
print(auto.pujc_auto())
print(auto.pujc_auto())

tachometr = input("Najetých kilometrů celkem: ")
pocetDni = input("Auto bylo půjčeno (počet dní): ")
celkovaCena = auto.vrat_auto(tachometr, pocetDni)
print(f"Celková cena za půjčení auta je {celkovaCena} Kč.")