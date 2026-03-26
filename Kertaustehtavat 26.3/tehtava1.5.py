def suurin_arvo(a, b, c):
    return max(a, b, c)

# käyttäjältä kysyminen
luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
luku3 = int(input("Anna luku 3: "))

print("Suurin arvo on:", suurin_arvo(luku1, luku2, luku3))