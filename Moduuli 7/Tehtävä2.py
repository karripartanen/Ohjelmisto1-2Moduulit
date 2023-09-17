#  Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes
#  käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma
#  tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö
#  nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
#  allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta
#  nimien tallentamiseen.

nimet = set()

nimi = input("Anna mikä vain nimi tai lopeta ohjelma antamalla tyhjä merkkijono: ")
if nimi != "":
    print("Uusi nimi")
    nimet.add(nimi)
while nimi != "":
    nimi = input("Anna mikä vain nimi tai lopeta ohjelma antamalla tyhjä merkkijono: ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    elif nimi not in nimet and nimi != "":
        print("Uusi nimi")
        nimet.add(nimi)
    if nimi == "":
        print("Syöttämäsi nimet:")
        for i in nimet:
            print(i)
