lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto (lisää, hae, lopeta): ").lower()

    if toiminto == "lisää":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "hae":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löydy")

    elif toiminto == "lopeta":
        print("Ohjelma päättyy")
        break

    else:
        print("Virheellinen valinta")

