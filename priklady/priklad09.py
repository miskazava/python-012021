vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

def ohodnot_studenta(znamky):
  suma = 0
  maTrojku = False
  for znamka in znamky:
    if type(znamky[znamka]) == int:
      suma += znamky[znamka]
      if znamky[znamka] == 5:
        return "Neprospel"
      elif znamky[znamka] == 3:
        maTrojku = True
  if suma / (len(znamky) - 1) <= 1.5 and not maTrojku:
    return "Prospel s vyznamenanim"
  else:
    return "Prospel"

for znamky in vysledky:
  prospech = ohodnot_studenta(znamky)
  print(znamky["Jméno"] + ": " + prospech)

