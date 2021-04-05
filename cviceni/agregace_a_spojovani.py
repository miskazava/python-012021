import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv")

import pandas

u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
maturita = pandas.concat([u202, u203, u302], ignore_index=True)
print(maturita.groupby('predmet')["znamka"].sum())

#print(maturita.head())
#maturita.to_csv("maturita.csv", index=False)
#maturita.to_excel("maturita.xlsx", index=False)

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")

#studenti = pandas.read_csv("studenti.csv")
#print(studenti.head())
#vysledky_se_jmeny = pandas.merge(u202, studenti, how="left")
#print(vysledky_se_jmeny.head())
#print(maturita.shape)
#print(vysledky_se_jmeny.shape)

#predsedajici = pandas.read_csv("predsedajici.csv")
#predsedajici["den"] = predsedajici["den"].str.strip()
#vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici, on="den")
#print(u202.shape)
#print(vysledky_se_jmeny_a_predsedajicimi.shape)