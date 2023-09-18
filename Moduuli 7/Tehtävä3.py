#  Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma
#  kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn
#  lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
#  ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun,
#  ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä
#  haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten
#  monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
#  (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman
#  ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

airports = {"EFHK": "Helsinki-Vantaa", "ESSA": "Arlandan lentoasema",
               "EDDF": "Frankfurt am Main", "EGLL": "Heathrow'n lentoasema"}
airport = ""
icao = ""
search = ""
question = "Komennot: NEW = Lisää lentokenttä, SEARCH = Etsi lentokenttää, END = lopeta ohjelma: "

command = input(question)
while command != "END":
    if command == "NEW":
        icao = input("Syötä lentokentän icao koodi: ")
        airport = input("Syötä lentokentän nimi: ")
        airports[icao] = airport
        command = input(question)
    if command == "SEARCH":
        search = input("Anna haluamasi lentokentän ICAO-koodi: ")
        if search in airports:
            print(f"Lentokentän nimi: {airports[search]}")
            command = input(question)
        else:
            print("Hakua vastaavaa lentokenttää ei löytynyt.")
            command = input(question)




