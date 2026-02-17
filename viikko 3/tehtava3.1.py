pituus = int(input("Anna kuhan pituus senttimetreinä:"))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")

else:
    print("Kuha on sallittua pyyntimittaa.")





