import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")
cenyAkcie = twilio["Close"]
cenyAkcie.plot()
plt.show()

twilio["Date"] = pandas.to_datetime(twilio["Date"])
cenyAkcie = twilio["Close"]
cenyAkcie.plot()
plt.show()


