import pandas
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv")
jmeno = pandas.read_csv('jmena.csv')
jmeno = jmeno.set_index("jméno")
#print(jmeno.loc["Jiří"])
#print(jmeno.loc[["Martin", "Zuzana", "Josef"]])
#print(jmeno.loc[:"Jiří"])
#print(jmeno.loc["Martin":"Tereza", "věk"])
#print(jmeno.loc["Libor":, "věk"])
print(jmeno.loc[:, "věk":"původ"])