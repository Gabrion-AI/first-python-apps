jedla = ["pizza", "rezne", "šalát"]

while True:
    print("\n--- MENU ---")
    print("1 - Zobraziť jedlá")
    print("2 - Pridať nové jedlo")
    print("3 - Skončiť")
    print("4 - Odstrániť jedlo")

    volba = input("Zvoľ možnosť (1-4): ")

    if volba == "1":
        print("\nTvoje oblúbené jedlá:")
        for jedlo in jedla:
            print("-", jedlo)

    elif volba == "2":
        nove_jedlo = input("Zadaj nové jedlo: ")
        jedla.append(nove_jedlo)
        print("Pridané:", nove_jedlo)

    elif volba == "3":
        print("Program sa ukončuje.")
        break

    elif volba == "4":
        odstranit = input("Zadaj názov jedla, ktoré chceš odstrániť: ")
        if odstranit in jedla:
            jedla.remove(odstranit)
            print("Odstránené:", odstranit)
        else:
            print("Toto jedlo nie je v zozname.")
    else:
        print("Neplatná voľba. Skús znova.")