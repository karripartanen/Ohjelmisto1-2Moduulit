#  Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
#  senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan
#  yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
#  halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
#  (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä
#  kirjoitettua funktiota.
import math


#  laskee neliöhinnan käyttäjän antamille pitsoille.
def bang_for_buck():
    pizza1_area = (math.pi*(((pizza1 / 100) / 2)*((pizza1 / 100) / 2)))
    sqr_meter = pizza1_area
    pizza1_value = price1 / sqr_meter
    pizza2_area = (math.pi * (((pizza2 / 100) / 2) * ((pizza2/100) / 2)))
    sqr_meter2 = pizza2_area
    pizza2_value = price2 / sqr_meter2
    if pizza1_value < pizza2_value:
        better_pizza = "Ensimmäinen antamasi pitsa on parempi hintalaatusuhteeltaan."
    elif pizza1_value == pizza2_value:
        better_pizza = "Pitsat ovat neliöhinnaltaan samanarvoisia, valitse kumpi vain!"
    else:
        better_pizza = "Toinen antamasi pitsa on parempi hintalaatusuhteeltaan."
    return better_pizza, pizza1_value, pizza2_value


pizza1 = float(input("Antaisitko ensimmäisen pitsan halkaisijan senttimetreinä: "))
price1 = float(input("Antaisitko ensimmäisen pitsan hinnan euroina: "))
pizza2 = float(input("Antaisitko toisen pitsan halkaisijan senttimetreinä: "))
price2 = float(input("Antaisitko toisen pitsan hinnan euroina: "))
print(f"{bang_for_buck()}")
