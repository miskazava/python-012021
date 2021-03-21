import pandas
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")
jobs = pandas.read_csv('DataAnalyst.csv')
print(jobs.columns)
print(jobs.shape)
print(jobs.loc[10])
print(jobs.loc[12:20, 'Job Title'])