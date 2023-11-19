import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Challenger-1971',
        autocommit=True
    )
    return connection

def get_icao(icao):
    connection = connect_db()
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        return result
    else:
        return 'Not found'
