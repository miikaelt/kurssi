while True:
    tuumat = float(input("Anna tuumat:"))

    if tuumat < 0:
        break
    cm = tuumat * 2.54
    print (f"{tuumat} tuumaa ={cm:.2f} cm")
