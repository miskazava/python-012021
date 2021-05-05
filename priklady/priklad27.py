import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

import pandas
vykazy = pandas.read_csv("vykazy.csv")
vykazyProjektu = vykazy.groupby("project").sum()
print(vykazyProjektu)