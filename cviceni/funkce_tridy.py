class Employee:
    def take_holiday(self, days):
        if self.holidays >= days:
            self.holidays -= days
            return "Dovolena schvalena"
        else:
            return f"Muzes si vzit pouze {self.holidays} dnu."

    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."

    def __str__(self):
        return self.name

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.holidays = 25

frantisek = Employee("Frantisek Novak", "konstrukter")
klara = Employee("KLara Nova", "sekretarka")
print(frantisek.take_holiday(10))
print(frantisek.take_holiday(10))
print(frantisek.take_holiday(10))

print(frantisek)

#frantisek = Employee()
#frantisek.name = "Frantisek Novak"
#frantisek.position = "konstrukter"

#klara = Employee()
#klara.name = "Klara Nova"
#klara.position = "sekretarka"

#print(frantisek.get_info())
#print(klara.get_info())