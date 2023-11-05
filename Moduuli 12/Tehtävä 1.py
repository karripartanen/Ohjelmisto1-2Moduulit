#  Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
#  Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
#  Käyttäjälle on näytettävä pelkkä vitsin teksti.
import json
import requests as req

# pyyntö satunnaiselle vitsille ja sen tulostus
request = "https://api.chucknorris.io/jokes/random"
response = req.get(request).json()
print(response['value'])
