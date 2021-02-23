schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}
sumOfMarks = 0
for mark in schoolReport.values():
    sumOfMarks += mark
print(f"Průměrná známka je {sumOfMarks/len(schoolReport)}.")

for x, y in schoolReport.items():
  if y == 1:
    print(x)
