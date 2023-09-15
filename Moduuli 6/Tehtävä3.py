#  Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
#  ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy
#  gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa
#  hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää
#  negatiivisen gallonamäärän.
#  Yksi gallona on 3,785 litraa.
gallons = 0
def gallon_to_liter():
    liters = gallons * 3.785
    return liters

while gallons >= 0:
    gallons = float(input("Convert gallons to liters. Provide the number of gallons: "))
    if gallons < 0:
        break
    else:
        gallon_to_liter()
        liters1 = gallon_to_liter()
        print(f"{gallons} gallons is {liters1} liters.")
