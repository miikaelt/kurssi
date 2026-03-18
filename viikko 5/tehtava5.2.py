luvut = []

while True:
    syote = input("Anna luku:")

    if syote == "":
        break
    luvut.append(float(syote))
luvut.sort(reverse=True)

print("Viisi suurinta lukua ovat:")

for luku in luvut[:5]:
    print(luku)
