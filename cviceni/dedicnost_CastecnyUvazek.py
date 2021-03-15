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

class PartTimeEmployee(Employee):
    def __init__(self, name, position, workload):
        super().__init__(name, position)
        self.workload = workload

    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}. Velikost uvazku je {self.workload}."

brigadnik = PartTimeEmployee("Jirka Pesik", "brigadnik ve skladu", 0.5)
print(brigadnik.get_info())