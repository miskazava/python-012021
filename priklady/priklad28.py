import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

import pandas

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")
euroStaty = staty[staty["region"] == "Europe"]
statySubregion = euroStaty.groupby("subregion").count()
print(statySubregion)
statySubregion = euroStaty.groupby("subregion").sum()
print(statySubregion)
