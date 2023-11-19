'''
minun_lista = [1,2,3,4,5,6,7]
print(minun_lista)

minun_monikko = (1,2,3,4,5,6,7)
print(minun_monikko)

minun_monikko2 = 1,2,(3,4),5,6
print(minun_monikko2)

minun_string = "fja3kdk"

minun_lista[0] = 0
print(minun_lista)
#  listan sisältöä voi muokata, monikkoa (tuple) ei voi


#  koodiesimerkki materiaalista

viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")

järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))

viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")

hedelmät = ("Appelsiini", "Banaani", "Omena")
(eka, toka, kolmas) = hedelmät
print(f"Hedelmiä ovat {eka}, {toka}, ja {kolmas}.")

#  Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa
#  järjestyksessä. Koska joukon alkioille ei ole määritelty järjestystä, ei alkioihin voi
#  myöskään viitata indeksillä. Toisin kuin listassa tai monikossa, sama alkio voi
#  esiintyä joukossa vain kertaalleen, eli joukossa ei voi olla kahta
#  samansisältöistä alkiota.

minun_monikko = (1,2,3,4,5,6,7)
print(minun_monikko)

minun_lista = [1,2,3,4,5,6,7]
print(minun_lista)

minun_joukko = {"Monopoly", "Shakki", "Cluedo"}
print(minun_joukko)

#  joukko (set) on järjestäytymätön tietorakenne

minun_joukko.add("Risk")
print(minun_joukko)

#  toisin kuin listassa ja monikossa, sama alkio voi esiintyä joukossa vain kertaalleen,
#  eli joukossa ei voi olla kahta samansisältöistä alkiota

minun_lista2 = [1,2,3,4,5,6,7]
print(minun_lista2)

minun_joukko2 = {1,2,3,4,5,6,7}

for i in minun_joukko2:
    print(i)
'''

#  sanakirja
##################

oppilaat = {'Aapeli': 24, 'Jenna': 43, 'Miro': 21, 'Heikki': 75}

for i in oppilaat:
    print(i)

#  arvot

for i in oppilaat:
    print(oppilaat[i])

oppilaat.items()

#  mitkä ovat avaimet sanakirjassa
print(oppilaat.keys)

#  mitkä ovat arvoja sanakirjassa
print(oppilaat.values)

print(oppilaat["Aapeli"])

oppilaat["Aapeliiiii"] = 43

nimi = input("anna nimi: ")
if nimi in oppilaat:
    print(f"Henkilö {nimi} ikä on {oppilaat[nimi]}")

#  poista tietue
del oppilaat["Aapeliiiii"]
print(oppilaat.items())

# toinen tapa poistaa tallentamalla se muuttujaan
aapelin_ikä = oppilaat.pop("Aapeli")
print(f"Aapeli poistettiin mutta ikä jäi talteen: {aapelin_ikä}")
print(oppilaat.items())

#  lisätään uusi oppilas jolla aapelin tiedot
oppilaat["Pekka"] = aapelin_ikä
print(oppilaat.items())
