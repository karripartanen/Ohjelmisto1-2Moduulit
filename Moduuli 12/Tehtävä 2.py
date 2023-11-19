#  Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma,
#  joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä
#  lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
#  Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan
#  API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
API_key = "703a400342c42feabcd15f9d56ce1937"
import json
import requests as req
query = True

while query == True:
    city_name = input("Provide the name of a city: ").strip()
    request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
    response = req.get(request)
    if response.status_code == 200:
        json_response = response.json()
        print(f"City: {json_response['name']}")
        print(f"Temperature: {json_response['main']['temp']-273.15:.1f} degrees Celsius.")
        print(f"Weather: {json_response['weather'][0]['main']}, ({json_response['weather'][0]['description']})")
        query = False
    else:
        print(f"Something went wrong, try again.\n")

