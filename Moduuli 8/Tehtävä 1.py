#  Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
#  Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan
#  kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna
#  airport-taulun ident-sarakkeeseen.

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='karripar',
    password='challenger71',
    autocommit=True
    )

def get_country_by_icao(icao):
    cursor = connection.cursor()
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return result
    else:
        return "NO RESULTS"

country = get_country_by_icao(input("Syötä maakoodi (ICAO): "))
print(f"Syöttämäsi ICAO koodia vastaava lentokenttä ja kunta: {country}.")