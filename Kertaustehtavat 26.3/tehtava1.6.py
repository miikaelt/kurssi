def summa(a, b):
    return a + b

def erotus(a, b):
    return a - b

def tulo(a, b):
    return a * b

def jako(a, b):
    if b != 0:
        return a / b
    else:
        return "Ei voi jakaa nollalla"

# käyttö
luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))

print("Summa:", summa(luku1, luku2))
print("Erotus:", erotus(luku1, luku2))
print("Tulo:", tulo(luku1, luku2))
print("Jako:", jako(luku1, luku2))