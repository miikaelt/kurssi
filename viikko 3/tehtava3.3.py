sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").strip().lower()
hb = int(input("Anna hemoglobiiniarvo (g/l):"))
if sukupuoli == "nainen":
    ala = 117
    yla = 175
    if hb < ala:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= yla:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    ala = 134
    yla = 195
    if hb < ala:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= yla:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
