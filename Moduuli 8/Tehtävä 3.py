#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu
# tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston
# avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään
# "geopy" ja vie asennus loppuun.

import mysql.connector
from geopy.distance import geodesic as GD

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='karripar',
    password='challenger71',
    autocommit=True
    )

def get_distance_between_icaos(icao):
    cursor = connection.cursor()
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return result
    else:
        return "NO RESULTS"

icao1 = get_distance_between_icaos(input("Provide the first ICAO code: "))
icao2 = get_distance_between_icaos(input("Provide the second ICAO code: "))
print(f"The distance between the two airports: {GD(icao1, icao2).km:.2f} kilometers.")

