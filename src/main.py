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
    """Получение всех мрашрутов"""
    return convert_all_object_to_json(models.Route, exclude=[models.Route.area])

@app.route('/routes/<pk>')
def get_detail_route(pk):
    """Получение детальной информации о маршруте с id = Pk"""
    return convert_all_object_to_json(
        models.Route.select().where(models.Route.id == int(pk))) 

@app.route('/routes', methods=['POST'])
def add_areas():
    """Создание нового района из json"""
    return create_object_from_json(models.Route, request.json)

@app.route('/routes/<pk>', methods=['DELETE'])
def del_areas(pk):
    models.Route.delete().where(models.Route.id == int(pk)).execute()
    """Удаление района из json"""
    return jsonify({'status': 'deleted'})



if __name__ == '__main__':
    app.run(debug=True)
