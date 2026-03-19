import math

def yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 2) / 100  # cm → m
    pinta_ala = math.pi * sade_m**2
    return hinta / pinta_ala

# pääohjelma
h1 = float(input("Anna pizzan 1 halkaisija (cm): "))
p1 = float(input("Anna pizzan 1 hinta (€): "))

h2 = float(input("Anna pizzan 2 halkaisija (cm): "))
p2 = float(input("Anna pizzan 2 hinta (€): "))

y1 = yksikkohinta(h1, p1)
y2 = yksikkohinta(h2, p2)

print("Pizza 1 €/m²:", y1)
print("Pizza 2 €/m²:", y2)

if y1 < y2:
    print("Pizza 1 on parempi vastine rahalle")
else:
    print("Pizza 2 on parempi vastine rahalle")