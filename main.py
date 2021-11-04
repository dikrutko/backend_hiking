from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/')
def main():
    return 'Перейти по <a href="/query/"> Запросу</a>'

def get(str):
    name = request.form.get("name")
    second = request.form.get('second')
    third = request.form.get('third')
    str = f'{name=}\n {second=}\n {third=}'
    #str1 = request.get_json()
    #str = jsonify(str1)
    return str 

def post():
    data = request.get_json()
    name = data['name']
    second = data['second']
    third = data['third']
    #str = f'{name=}\n{second=}\n{third=}'
    str = f'"name": "{name}", "second": "{second}", third": {third}'
    return str

@app.route('/query/', methods=['GET', 'POST'])
def query():
    #str = '{"name": "asdqw", "second": "qwezx", "third": 12345}'
    str = ''
    if request.method == 'POST':
        str = str + post()
        return str
    if request.method == 'GET':
        return get(str)
       
if __name__ == '__main__':
    app.run(debug=True)