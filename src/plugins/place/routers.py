from flask import jsonify, request
from plugins.core.plugin_manager import PluginManager
from plugins.place.models import Place
from utils import convert_all_object_to_json, create_object_from_json

manager = PluginManager(None)


@manager.route('/places', methods=['GET'])
def get_places():
    """Получение всех маршрутов"""
    return convert_all_object_to_json(Place, exclude=[Place.area])

@manager.route('/places/<pk>')
def get_detail_places(pk):
    """Получение детальной информации о маршруте с id = Pk"""
    return convert_all_object_to_json(
        Place.select().where(Place.id == int(pk))) 

@manager.route('/places', methods=['POST'])
def add_places():
    """Создание нового маршрута из json"""
    return create_object_from_json(Place, request.json)

@manager.route('/places/<pk>', methods=['DELETE'])
def del_places(pk):
    Place.delete().where(Place.id == int(pk)).execute()
    """Удаление маршрута из json"""
    return jsonify({'status': 'deleted'})
