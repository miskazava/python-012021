prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
kniha = input("Zadej název knihy: ")
if kniha in prodeje2019:
    if kniha in prodeje2020:
        prodejCelkem = prodeje2019[kniha] + prodeje2020[kniha]
        print(f"Celkem se prodalo {prodejCelkem} ks.")
    else:
        print(f"Celkem se prodalo {prodeje2019[kniha]} ks.")
else:
    if kniha in prodeje2020:
        print(f"Celkem se prodalo {prodeje2020[kniha]} ks.")
    else:
        print(f"Celkem se prodalo 0 ks.")