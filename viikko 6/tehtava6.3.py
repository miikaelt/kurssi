def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


while True:
    gall = float(input("Anna gallonamäärä: "))

    if gall < 0:
        break

    litrat = gallonat_litroiksi(gall)
    print("Litroina:", litrat)