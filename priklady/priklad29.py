import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperature = pandas.read_csv("temperature.csv")
trinastyListopad = temperature[temperature["Day"] == 13]
trinastyListopad = trinastyListopad[trinastyListopad.AvgTemperature != -99]
regionData = trinastyListopad.groupby("Region").count()
regionPrumer = trinastyListopad.groupby("Region").mean()
regionMax = trinastyListopad.groupby("Region").max()
regionMin = trinastyListopad.groupby("Region").min()
