sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
print("Vydané knížky: ")
for key in sales:
    print(key)
total = 0
for key, value in sales.items():
    print(f"Knihy {key} se prodalo {value} kusů.")
    total += value
    # total = total + value
print(f"Celkem bylo prodáno {total} knih.")
print("Celkem bylo prodáno " + str(total) + " knih.")
##cviceni 2
books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
total = 0
for item in books:
    if item["year"] == 2019:
        total += item["sold"] * item["price"]
print(f"Celkové tržby jsou {total}.")

