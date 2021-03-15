class Auto:
    def __init__(self, registracniZnacka, znacka, typVozidla, pocetKilometru):
        self.registracniZnacka = registracniZnacka
        self.znacka = znacka
        self.typVozidla = typVozidla
        self.pocetKilometru = pocetKilometru
        self.volne = True

    def obsazenost(self):
        self.volne = False

auto1 = Auto("4A2 3020", "Peugeot", "403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda", "Octavia", 41253)
