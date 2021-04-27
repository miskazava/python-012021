#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
temperature = pandas.read_csv("temperature.csv")
print(temperature)
print(temperature[temperature["Day"] == 13])
novemberThirteen_US = temperature[(temperature["Day"] == 13) & (temperature["Country"] == "US")]
print(novemberThirteen_US)
print(novemberThirteen_US[(novemberThirteen_US["City"] == "Washington") | (novemberThirteen_US["City"] == "Philadelphia")])