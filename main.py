from flask import Flask, request, jsonify
from flask.json import dumps
import models

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

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


@app.route('/news', methods=['GET'])
def get_news():
    result = []

    for news in models.News.select():
        result.append(news.to_json())
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
