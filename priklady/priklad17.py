class Polozka:

    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        return f"název filmu: {self.nazev}, žánr: {self.zanr}"


class Film(Polozka):

    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = int(delka)

    def get_info(self):
        super().get_info()
        return super().get_info() + f", délka: {self.delka}"

    def get_celkova_delka(self):
        celkova_delka = int(self.delka)
        return celkova_delka

class Serial(Polozka):

    def __init__(self, nazev, zanr, pocetEpizod, delkaEpizody):
        super().__init__(nazev, zanr)
        self.pocetEpizod = pocetEpizod
        self.delkaEpizody = delkaEpizody

    def get_info(self):
        super().get_info()
        return super().get_info() + f"počet epizod: {self.pocetEpizod}, délka epizódy: {self.delkaEpizody}"

    def get_celkova_delka(self):
        celkova_delka = self.pocetEpizod * self.delkaEpizody
        return celkova_delka

class Uzivatel:

    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0

    def pripocti_zhlednuti(self, celkova_delka):
        self.delka_sledovani += celkova_delka
        return self.delka_sledovani

malezeny = Film("Malé ženy", "drama", 165)
biglittlelies = Serial("Sedmilhářky", "krimi", 7, 60)
misa = Uzivatel("misa")
misa.pripocti_zhlednuti(malezeny.get_celkova_delka())
misa.pripocti_zhlednuti(biglittlelies.get_celkova_delka())
print(misa.delka_sledovani)