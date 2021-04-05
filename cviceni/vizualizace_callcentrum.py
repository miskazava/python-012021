import matplotlib.pyplot as plt
import pandas
import datetime as dt

callcentrum = pandas.read_csv("callcentrum.txt", header=None)
callcentrum = callcentrum[0].str.split(':', expand=True).astype(int)
callcentrum['seconds'] = callcentrum[0] * 60 + callcentrum[1]
print(callcentrum.head())
callcentrum['seconds'].hist()
callcentrum['seconds'].plot(kind='box')
plt.show()

#callcentrum = pandas.read_csv("callcentrum.txt", header=None)
#callcentrum["seconds"] = pandas.to_datetime(callcentrum[0], format="%M:%S")
#fig = callcentrum["seconds"].hist()
#fig.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))
#plt.show()
