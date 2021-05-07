import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperature = pandas.read_csv("temperature.csv")
trinastyListopad = temperature[temperature["Day"] == 13]
trinastyListopad = trinastyListopad[trinastyListopad.AvgTemperature != -99]
razeni = trinastyListopad.sort_values(by="AvgTemperature", ascending=False)
print(razeni.iloc[:5])
print(razeni.iloc[-5:])