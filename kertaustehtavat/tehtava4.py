tarina = []
edellinen = None

while True:
    sana = input("Anna sana lisättäväksi tarinaan:")

    # bonus: sama sana kahdesti peräkkäin
    if edellinen is not None and sana == edellinen:
        print(" ".join(tarina))
        break

    if sana == "loppu":
        print(" ".join(tarina))
        break

    tarina.append(sana)
    edellinen = sana


