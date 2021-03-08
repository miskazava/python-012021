class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def getInfo(self):
        return f"Kniha {self.title} ma {self.pages} stran. Cena je {self.price} Kc."

    def discount(self, amount):
        self.price -= self.price * (amount/100)


hamlet = Book("Hamlet", 283, 199)
print(hamlet.getInfo())
hamlet.discount(50)
print(hamlet.getInfo())