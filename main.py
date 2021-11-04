from flask import Flask, request
from flask.json import dumps

app = Flask(__name__)
newbase = []

def get():
    return dumps(newbase) 

def post():#add
    name = request.form.get('name')
    second = request.form.get('second')
    third = (request.form.get('third'))
    new = {
        'name': name,
        'second': second,
        'third': third,
    }
    newbase.append(new)
    return dumps(new)

@app.route('/', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        return post()
    if request.method == 'GET':
        return get()
       
if __name__ == '__main__':
    app.run(debug=True)