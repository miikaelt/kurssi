def poista_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

# pääohjelma
lista = [1, 2, 3, 4, 5, 6, 7]

suodatettu = poista_parittomat(lista)

print("Alkuperäinen:", lista)
print("Parilliset:", suodatettu)