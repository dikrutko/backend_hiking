from flask import jsonify, request
from plugins.core.plugin_manager import PluginManager
from plugins.route.models import Route
from utils import convert_all_object_to_json, create_object_from_json

manager = PluginManager(None)

@manager.route('/routes', methods=['GET'])
def get_routes():
    """Получение всех маршрутов"""
    return convert_all_object_to_json(Route, exclude=[Route.area, Route.points])

@manager.route('/routes/<pk>')
def get_detail_routes(pk):
    """Получение детальной информации о маршруте с id = Pk"""
    return convert_all_object_to_json(
        Route.select().where(Route.id == int(pk))) 

@manager.route('/routes', methods=['POST'])
def add_routes():
    """Создание нового маршрута из json"""
    return create_object_from_json(Route, request.json)

@manager.route('/routes/<pk>', methods=['DELETE'])
def del_routes(pk):
    Route.delete().where(Route.id == int(pk)).execute()
    """Удаление маршрута из json"""
    return jsonify({'status': 'deleted'})