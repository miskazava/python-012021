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

auto1 = Auto("4A2 3020", "Peugeot", "403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda", "Octavia", 41253)

znacka = input("Zadej značku auta, o kterou máš zájem (Peugeot/Škoda): ")
print(auto2.get_info())
print(auto2.pujc_auto())
print(auto2.pujc_auto())