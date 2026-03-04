tuntipalkka = float(input("Tuntipalkka:"))
tunnit = float(input("Tehdyt tunnit:"))
paiva = input("Viikonpaiva:").strip().lower()

if paiva == "Sunnuntai":
    paivapalkka = (tuntipalkka * 2) * tunnit
else:
    paivapalkka = tuntipalkka * tunnit
print(f"Paivapalkka: {paivapalkka} euroa")
