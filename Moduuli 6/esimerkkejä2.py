#  funktiot jatkuu 12.9.2023
'''
def print_city(city3):
    # lokaali muuttuja, arvo käytössä vain funktion sisällä (local scope)
    city = "Helsinki"  #  globaali muuttuja korvataan lokaalilla
    city2 = "Vantaa"
    print(city)
    print(city2)
    print(city3)  # myös funktion parametrina esitelty muuttuja on lokaali

def print_city_v2():
    print(city)  #  tulostaa globaalin muuttuja arvon

#  globaali muuttuja, arvo käytössä koko ohjelman laajuisesti (global scope)'
#  (jossei sitä "ylikirjoiteta (shadows)" funktion sisällä)
city = "Espoo"
print_city("Kirkkonummi")
print_city("Vihti")
print(city)
#  print(city2)  #  city2 ei näy globaalisti, koska määritelty funktion sisällä
print_city_v2()
'''

