#  Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän
#  nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
#  Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
#  Vastauksen on oltava muodossa:
#  {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask as Flask, request, Response
import json
import database_call


app = Flask(__name__)


@app.route('/')
def get_root():
    return 'No terve!'

@app.route('/airport/<icao>')

def icao_to_data(icao):
    try:
        airport, city = database_call.get_icao(icao)
        status_code = 200
        response_data = {
            "ICAO": icao,
            "NAME": airport,
            "MUNICIPALITY": city
        }

    except ValueError:
        response_data = {
            'msg': 'Invalid ICAO-code'
        }
        status_code = 400

    response_data = json.dumps(response_data)
    #  setting up a status code for response requires Response object to be created
    response = Response(response=response_data, status=status_code, mimetype='application/json')
    return response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "status": "404",
        "text": "Unknown domain"
    }
    jsonresp = json.dumps(response)
    return Response(response=jsonresp, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
    