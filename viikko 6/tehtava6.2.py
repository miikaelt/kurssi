import random

def heita_noppa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen määrä: "))
maksimi = int(input("Anna tavoitesilmäluku: "))

while True:
    silmaluku = heita_noppa(tahkot)
    print("Heitto:", silmaluku)
    if silmaluku == maksimi:
        break
