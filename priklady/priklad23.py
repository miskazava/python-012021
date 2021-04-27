#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
import pandas
vaccinations = pandas.read_csv("country_vaccinations.csv")
#vaccinations = vaccinations.set_index("country")
print(vaccinations.columns)
desaty_brezen = vaccinations[vaccinations["date"] == "2021-03-10"]
print(desaty_brezen[["country", "total_vaccinations"]])
hodne_vakcin = vaccinations[(vaccinations["date"] == "2021-03-10") & (vaccinations["total_vaccinations"] > 1000000)]
print(hodne_vakcin[["country", "total_vaccinations"]])
den_max = vaccinations[vaccinations["daily_vaccinations"] > 100000]
print(den_max)
den_min = vaccinations[vaccinations["daily_vaccinations"] < 100]
print(den_min)