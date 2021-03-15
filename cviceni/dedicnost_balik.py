class Package:
    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def get_info(self):
        if self.delivered:
            return f"Balik na adresu {self.address} s vahou {self.weightInKilos} kg byl dorucen."
        return f"Balik na adresu {self.address} s vahou {self.weightInKilos} kg nebyl dorucen."

class ValuablePackage(Package):
    def __init__(self, address, weightInKilos, value):
        super().__init__(address, weightInKilos)
        self.value = value

balik = ValuablePackage("Krymska", 11, 560)
print(balik.get_info())
balik.deliver()
print(balik.get_info())
