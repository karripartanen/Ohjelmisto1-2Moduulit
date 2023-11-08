#  Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
#  Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua
#  31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
#  Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/')
def get_root():
    return 'Hello there!'


def prime_number(num):
    if num <= 1:
        return False
    elif num in (2, 3):
        return True
    for i in (2, 3, 5, 7):
        if num % i == 0:
            return False
    return True


@app.route('/alkuluku/<num>')
def prime(num):
    try:
        num = int(num)
    except ValueError:
        response_data = {
            'msg': 'input invalid',
            'input': num
        }
        status_code = 400
    else:
        result = prime_number(num)
        #  response in dictionary format is translated to json automatically
        response_data = {
            'msg': 'Calculation done',
            'input_num': num,
            'Prime number': result
        }
        status_code = 200

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
    jsonresponse = json.dumps(response)
    return Response(response=jsonresponse, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
