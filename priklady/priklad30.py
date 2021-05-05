import pandas
vykazy = pandas.read_csv("vykazy.csv")
vykazy.to_excel("output.xlsx")
vykazyExcel = pandas.read_excel("output.xlsx")
print(vykazyExcel)