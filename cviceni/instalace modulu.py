#import wget
#wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

import pandas
nakupy = pandas.read_csv('nakupy.csv')
#nakupy.info()
print(nakupy.shape)
print(nakupy.shape[0])
print(nakupy.columns)
print(nakupy.iloc[3])