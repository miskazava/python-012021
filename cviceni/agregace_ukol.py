import wget

#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/jmena.csv')
#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti1.csv')
#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti2.csv')

import pandas
studenti1 = pandas.read_csv("studenti1.csv").dropna()
studenti2 = pandas.read_csv("studenti2.csv").dropna()
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
#print(studenti.head())
#print(studenti.columns)

chyba1 = studenti[studenti['ročník'].isnull()]
#print(f"Chybí ročník, nestuduje: {len(chyba1)}")
#print(chyba1.shape)

chyba2 = studenti[studenti['kruh'].isnull()]
#print(f"Chybí skupina, studuje dálkově: {len(chyba2)}")
#print(chyba2.shape)

studenti = studenti.dropna()

obor = studenti.groupby('obor').count()
#print(obor)

prospech = studenti.groupby('obor')['prospěch'].mean()
#print(prospech)

jmena = pandas.read_csv('jmena.csv').dropna()

propojeni = pandas.merge(jmena, studenti, how='left')

pohlavi = propojeni.groupby('pohlaví').count()
print(pohlavi)

it_gender = propojeni.groupby('pohlaví').count()