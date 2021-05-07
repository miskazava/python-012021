import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import pandas
velikonoce = pandas.read_csv("velikonoce.csv")

import matplotlib.pyplot as plt
ax = velikonoce.plot(kind='bar', color='pink', grid=True)
ax.set_ylabel("Počet dnů")
ax.set_xlabel("Datumy")
plt.show()