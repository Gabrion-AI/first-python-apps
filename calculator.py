print("Vitaj v kalkulačke!")
print("Vyber si operáciu:")
print("1 - Sčítanie")
print("2 - Odčítanie")
print("3 - Násobenie")
print("4 - Delenie")

volba = input("Zadaj číslo operácie (1/2/3/4): ")

cislo1 = float(input("Zadaj prvé číslo: "))
cislo2 = float(input("Zadaj druhé číslo: "))

if volba == "1":
    vysledok = cislo1 + cislo2
    print("Výsledok:", vysledok)
elif volba == "2":
    vysledok = cislo1 - cislo2
    print("Výsledok:", vysledok)
elif volba == "3":
    vysledok = cislo1 * cislo2
    print("Výsledok:", vysledok)
elif volba == "4":
    if cislo2 != 0:
        vysledok = cislo1 / cislo2
        print("Výsledok:", vysledok)
    else:
        print("Chyba: Nedá sa deliť nulou.")
else:
    print("Zadal si neplatnú voľbu.")