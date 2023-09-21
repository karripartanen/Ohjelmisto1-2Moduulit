#  Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
#  tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
#  Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä
#  on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='karripar',
    password='challenger71',
    autocommit=True
    )

def get_airport_count_by_iso_code(country_code):

    cursor = connection.cursor()
    sql = f"SELECT type FROM airport WHERE iso_country = '{country_code}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    small = 0
    medium = 0
    large = 0
    heli = 0
    for i in result:
        if i[0] == "small_airport":
            small += 1
        elif i[0] == "medium_airport":
            medium += 1
        elif i[0] == "large_airport":
            large += 1
        elif i[0] == "heliport":
            heli += 1
    if result:
        return small, medium, large, heli
    else:
        return "NO RESULTS"

country = get_airport_count_by_iso_code(input("Anna maakoodi: "))
small, medium, large, heli = country
print(f"Small airports = {small}, medium airports = {medium}, large airports = {large},"
      f" heliports = {heli}.")

