"""
def tervehdi():
    print("Moi!")
    print("nyt ollaan funktion sisällä, ohjelman suoritus siirtyi tänne")
    return


#  pääohjelma
#  jotta funtiossa olevaa koodia suoritettaisiin, on funktiota kutsuttava
print("moi, tämä on pääohjelma")
#  funktion kutsu
tervehdi()
print("jonka jälkeen tulimme takaisin pääohjelmaan")

#  funktio voi kutsua muita funktioita

def tervehdi_kayttajaa():
    print("moi taas")
    return

def main():
    tervehdi_kayttajaa()
    return

main()

#######2
#  kerrat on parametrimuuttuja
def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
#  annetaan argumenttina 5
tervehdi(5)
print ("Tervehditään lisää.")
tervehdi(2)

kertaa = int(input("montako kertaa tervehditään: "))
tervehdi(kertaa)
"""

#  funktion parametrit ja paluuarvo
#########3
def printtaa_summa(x, y):
    print(x+y)
    return

#  funktiolle voi välittää useampia argumentteja
#  tämä funktio ei palauta mitään, joskus se on ihan ok
printtaa_summa(5,8)

def summa2(x, y):
    yht = x + y
    return yht

tulos = summa2(5,8)
print(tulos)

def tietoja(nimi, ikä, harrastus):
    tervehdys = f"terve {nimi}, ikäsi on {ikä} ja suosikkiharrastus on {harrastus}"
    return tervehdys

henkilö = tietoja("Karri", 21, "Kuntosalitreenaus")
print(henkilö)

henkilö2 = tietoja(nimi = "Pekka", ikä = 23, harrastus = "Jääkiekko")
print(henkilö2)

# mitä jos en tiedä jotain argumenttia, miten voin kutsua funktiota?

def tietoja2(nimi, ikä, harrastus='ohjelmointi'):
    tervehdys = f"terve {nimi}, ikäsi on {ikä} ja suosikkiharrastus on {harrastus}"
    return tervehdys

henkilö3 = tietoja2("Pekka", 23)
print(henkilö3)
