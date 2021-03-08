def company_points(industry, turnover, country, conference=False, newsletter=False):
    points = 0
    if industry == "automotive":
        points += 3
    elif industry == "retail":
        points += 2
    if turnover >= 10 and turnover <= 1000:
        points += 3
    elif turnover > 1000:
        points += 1
    if country == "Czechia" or country == "Slovakia":
        points += 2
    elif country == "Germany" or country == "France":
        points += 1
    if conference:
        points += 1
    if newsletter:
        points += 1
    return points

evaluation = company_points("retail", 15, "Slovakia", True)
if evaluation <= 5:
    chance = "Sance na ziskani je mala."
if evaluation > 5 and evaluation <= 8:
    chance = "Sance na ziskani je stredni."
if evaluation > 8:
    chance = "Sance na ziskani je velka."

print(chance)



#company_points(industry, turnover, country, conference=False, newsletter=False)