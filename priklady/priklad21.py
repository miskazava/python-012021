import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
twilio = pandas.read_csv('twlo.csv')
print(twilio.shape)
print(twilio.iloc[:5])
print(twilio.head(n=5))
print(twilio.tail(n=1))
pocet_radku = int(twilio.shape[0])
print(pocet_radku)
prvni_zaviraci_hodnota = twilio.iloc[0, 5]
print(prvni_zaviraci_hodnota)
posledni_zaviraci_hodnota = twilio.iloc[301, 5]
print(posledni_zaviraci_hodnota)
hodnota = posledni_zaviraci_hodnota / prvni_zaviraci_hodnota * 100 - 100
print(hodnota)
sloupce_high = twilio["High"]
print(sloupce_high)
sloupce_low = twilio["Low"]
print(sloupce_low)