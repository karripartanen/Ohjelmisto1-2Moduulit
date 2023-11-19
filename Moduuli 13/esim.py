from flask import Flask as Flask, request, Response
import json

aparaatti = Flask(__name__)


@aparaatti.route('/')
def get_root():
    return 'Bollocks'


#  example query: http://localhost:3000/kukkuu?name=Matti&age=21
@aparaatti.route('/kukkuu')
def get_kukkuu():
    print(request.args)
    name = request.args.get('name')
    age = request.args.get('age')
    return f'kukkuuuuuuuuuuu {name}, {age} vuotta vanha!'


#  example query: http://localhost:3000/kukkuu/Matti/21
@aparaatti.route('/kukkuu/<name>/<age>')
def get_kukkuu_v2(name, age):
    return f'kukkuuuuuuuuuuu {name}, {age} vuotta vanha!'


#  example query: http://localhost:3000/multiply/5
#  example response {input_num: 5, result: 25}
#  num must be between 0-100
@aparaatti.route('/multiply/<num>')
#  TODO: refactor code: create response object and return it only once
def multiply(num):
    try:
        num = float(num)
    except ValueError:
        response_data = {
            'msg': 'input invalid',
            'input': num
        }
        status_code = 400
    else:

        if 0 < num <= 100:
            result = num * num
            #  response in dictionary format is translated to json automatically
            response_data = {
                'msg': 'Calculation done',
                'input_num': num,
                'result': result
            }
            status_code = 200

        else:
            response_data = {
                'msg': 'input out of bounds',
                'input_num': num
            }
            status_code = 400

    response_data = json.dumps(response_data)
    #  setting up a status code for response requires Response object to be created
    response = Response(response=response_data, status=status_code, mimetype='application/json')
    return response

@aparaatti.errorhandler(404)
def page_not_found(error_code):
    response = {
        "status": "404",
        "text": "Unknown domain"
    }
    jsonresp = json.dumps(response)
    return Response(response=jsonresp, status=404, mimetype="application/json")


if __name__ == '__main__':
    aparaatti.run(use_reloader=True, host='127.0.0.1', port=3000)
