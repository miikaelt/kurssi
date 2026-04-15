# Vuodenajat kuukausittain (1–12)
# Joulukuu aloittaa talven
vuodenajat = (
    "talvi",  # tammikuu (1)
    "talvi",  # helmikuu
    "kevät",  # maaliskuu
    "kevät",  # huhtikuu
    "kevät",  # toukokuu
    "kesä",   # kesäkuu
    "kesä",   # heinäkuu
    "kesä",   # elokuu
    "syksy",  # syyskuu
    "syksy",  # lokakuu
    "syksy",  # marraskuu
    "talvi"   # joulukuu
)

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print(vuodenajat[kuukausi - 1])
else:
    print("Virheellinen kuukausi")