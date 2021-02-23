def greetUser(name):
    print(f"Ahoj! {name}")
greetUser("Jirko")

def sumTwoNumbers(a, b):
    return a + b
result = sumTwoNumbers(5, 9)
print(result)

def getMark(points, bonus=0):
  if points + bonus <= 60:
    mark = 5
  elif points + bonus <= 70:
    mark = 4
  elif points + bonus <= 80:
    mark = 3
  elif points + bonus <= 90:
    mark = 2
  else:
    mark = 1
  return mark
points = input("Zadej pocet bodu: ")
points = int(points)
bonus = input("Zadej pocet bonusovych bodu: ")
bonus = int(bonus)
mark = getMark(points, bonus)
if mark == 5:
    points = input("Pocet bodu z opravneho testu: ")
    points = int(points)
    mark = getMark(points)
print(f"Vysledna znamka je {mark}.")