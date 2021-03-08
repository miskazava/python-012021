class Employee:

    def get_info(self):
        if self.probation:
            return f"{self.name} pracuje na pozici {self.position}. Zamestnanec je ve zkusebni lhute."
        return f"{self.name} pracuje na pozici {self.position}."

    def __str__(self):
        return self.name

    def __init__(self, name, position):
        namer = name
        self.name = name
        self.position = position
        self.probation = False

    def setProbation(self):
        self.probation = True



frantisek = Employee("Frantisek Novak", "konstrukter")
klara = Employee("KLara Nova", "sekretarka")
frantisek.setProbation()
print(frantisek.get_info())
print(klara.get_info())