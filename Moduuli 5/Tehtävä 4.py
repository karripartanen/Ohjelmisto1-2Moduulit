# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet
# yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa
# ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan
# allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta
# nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

i = 0  # Iterator (i) keeps count in the for-loop
city_str = ""
cities = []
for i in range(5):
    city_str = input("Provide a name of a city: ")
    cities.append(city_str)

print("Cities you entered to the program")
for city_str in cities:
    print(city_str)


