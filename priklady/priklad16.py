class Polozka:

    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        return f"název filmu: {self.nazev}, žánr: {self.zanr}")


class Film(Polozka):

    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = int(delka)

    def get_info(self):
        return self.nazev, self.zanr, self.delka

class Serial(Polozka):

    def __init__(self, nazev, zanr, pocetEpizod, delkaEpizody):
        super().__init__(nazev, zanr)
        self.pocetEpizod = int(pocetEpizod)
        self.delkaEpizody = int(delkaEpizody)

    def get_info(self):
        return self.nazev, self.zanr, self.pocetEpizod, self.delkaEpizody

malezeny = Film("Malé ženy", "drama", 165)
print(malezeny.get_info())