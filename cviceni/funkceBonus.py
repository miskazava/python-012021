def monthOfBirth(rodcislo):
    rodcislo = str(rodcislo)
    mesic = rodcislo[2] + rodcislo[3]
    mesic = int(mesic)
    if mesic > 50:
        mesic -= 50
    return mesic
result = monthOfBirth(860520)
print(result)