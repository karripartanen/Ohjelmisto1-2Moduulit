import mysql.connector
#  CREATE USER IF NOT EXISTS 'karripar'@'localhost' IDENTIFIED BY 'challenger71';
#  GRANT ALL PRIVILEGES ON `flight_game`.* TO 'karripar'@'localhost';

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='karripar',
    password='challenger71',
    autocommit=True
    )
'''
cursor = connection.cursor()
#  cursor.execute("SELECT iso_country, name FROM country WHERE iso_country = 'FI'")
#  result = cursor.fetchall()
#  print(result)

cursor.execute("SELECT iso_country, name FROM country")
result = cursor.fetchall()
print(cursor.rowcount)  #  tulosrivien määrä
print(result)  #  koko tulosjoukko listana

for country in result:  #  country: yksi tulosjoukon rivi tuplena
    print(f"Maa: {country[1]}, koodi: {country[0]}")
'''
def get_country_by_iso_code(iso_code):
    cursor = connection.cursor()
    sql = f"SELECT iso_country, name FROM country WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return result[1]
    else:
        return "NO RESULTS"

country = get_country_by_iso_code('FI')
print(country)
country = get_country_by_iso_code(input("Syötä maakoodi: "))
print(country)

#  päivitetään maiden nimiä kannassa
def update_country_by_iso_code(iso_code, country_name):
    cursor = connection.cursor()
    sql = f"UPDATE country SET name='{country_name}' WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    if cursor.rowcount > 0:
        return f"Koodi {iso_code} päivitetty, uusi maan nimi: {country_name}"
    else:
        return f"Koodia {iso_code} ei löytynyt"

country_code = input("Anna muokattava koodi: ")
new_name = input("Anna maalle uusi nimi: ")
update_country_by_iso_code(country_code, new_name)

