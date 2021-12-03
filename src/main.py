from flask import Flask, request, jsonify
from flask.json import dumps
import models
from playhouse.shortcuts import model_to_dict, dict_to_model
from peewee import IntegrityError
from utils import convert_all_object_to_json, create_object_from_json


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/news', methods=['GET'])
def get_news():
    """Получение всех новостей"""
    return convert_all_object_to_json(models.News)

@app.route('/news', methods=['POST'])
def add_news():
    """Создание новой новости из json"""
    return create_object_from_json(models.News, request.json)

@app.route('/news/<pk>', methods=['DELETE'])
def del_news(pk):
    models.News.delete().where(models.News.id == int(pk)).execute()
    """Удаление новости из json"""
    return jsonify({'status': 'deleted'})

@app.route('/news_vk', methods=['POST'])
def load_news_from_vk():
    #{ "type": "confirmation", "group_id": 126669581 }
    #5aa2565d
    if not request.json:
        return 'hello'
    if request.json.get('type') == 'confirmation':
        return '5aa2565d'
    return 'hello'


@app.route('/areas', methods=['GET'])
def get_areas():
    """Получение всех районов"""
    return convert_all_object_to_json(models.Area)

@app.route('/areas', methods=['POST'])
def add_areas():
    """Создание нового района из json"""
    return create_object_from_json(models.Area, request.json)

@app.route('/areas/<pk>', methods=['DELETE'])
def del_areas(pk):
    models.Area.delete().where(models.Area.id == int(pk)).execute()
    """Удаление района из json"""
    return jsonify({'status': 'deleted'})


@app.route('/routes', methods=['GET'])
def get_routes():
    """Получение всех маршрутов"""
    return convert_all_object_to_json(models.Route, exclude=[models.Route.area])

@app.route('/routes/<pk>')
def get_detail_routes(pk):
    """Получение детальной информации о маршруте с id = Pk"""
    return convert_all_object_to_json(
        models.Route.select().where(models.Route.id == int(pk))) 

@app.route('/routes', methods=['POST'])
def add_routes():
    """Создание нового маршрута из json"""
    return create_object_from_json(models.Route, request.json)

@app.route('/routes/<pk>', methods=['DELETE'])
def del_routes(pk):
    models.Route.delete().where(models.Route.id == int(pk)).execute()
    """Удаление маршрута из json"""
    return jsonify({'status': 'deleted'})


@app.route('/places', methods=['GET'])
def get_places():
    """Получение всех маршрутов"""
    return convert_all_object_to_json(models.Place, exclude=[models.Place.area])########## route?

@app.route('/places/<pk>')
def get_detail_places(pk):
    """Получение детальной информации о маршруте с id = Pk"""
    return convert_all_object_to_json(
        models.Place.select().where(models.Place.id == int(pk))) 

@app.route('/places', methods=['POST'])
def add_places():
    """Создание нового маршрута из json"""
    return create_object_from_json(models.Place, request.json)

@app.route('/places/<pk>', methods=['DELETE'])
def del_places(pk):
    models.Place.delete().where(models.Place.id == int(pk)).execute()
    """Удаление маршрута из json"""
    return jsonify({'status': 'deleted'})


@app.route('/team', methods=['GET'])
def get_team():
    """Получение всех людей из командв"""
    return convert_all_object_to_json(models.Team)

@app.route('/team', methods=['POST'])
def add_team():
    """Добавление нового человека в команду из json"""
    return create_object_from_json(models.Team, request.json)

@app.route('/team/<pk>', methods=['DELETE'])
def del_team(pk):
    models.Team.delete().where(models.Team.id == int(pk)).execute()
    """Удаление человека из команды из json"""
    return jsonify({'status': 'deleted'})


if __name__ == '__main__':
    app.run(debug=True)
