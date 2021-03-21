import pandas
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
nakupy = pandas.read_csv('nakupy.csv')
#print(nakupy.iloc[8:])
#print(nakupy.iloc[-3:])
pozdrav = "Ahoj Andreo"
#print(pozdrav[-6:-3])
#print(pozdrav.strip().replace(" ", ""))
#print(nakupy.head(n=3))
#print(nakupy.tail(n=2))
print(nakupy.iloc[:, [0, 3]])