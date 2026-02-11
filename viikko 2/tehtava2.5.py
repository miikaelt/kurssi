leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = (leiviskat * 20 * 32 *13.3 + naulat * 32 * 13.3 + luodit *13.3)

kilot = int(grammat // 1000)
grammat_loput = grammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilot} kg ja {grammat_loput: .2f} g")




