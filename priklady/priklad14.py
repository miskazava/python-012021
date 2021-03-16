class Employee:

    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."

    def __init__(self, name, position, salary, children):
        self.name = name
        self.position = position
        self.salary = 100000
        self.children = 2

    def get_net_salary(self):
        salary = self.salary
        children = self.children
        netSalary = salary - (salary * 0.15 - children * 1500)
        return netSalary

michal = Employee("Michal Voda", "software developer", 100000, 2)
print(michal.get_info())
print(michal.get_net_salary())
