import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import pandas
platy = pandas.read_csv("platy_2021_02.csv")

import matplotlib.pyplot as plt
platy.hist()
plt.show()