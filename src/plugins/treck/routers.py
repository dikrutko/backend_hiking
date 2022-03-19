from flask import jsonify, request
from plugins.core.plugin_manager import PluginManager
from plugins.treck.models import Treck
from utils import convert_all_object_to_json, create_object_from_json

manager = PluginManager(None)

@manager.route('/trecks', methods=['GET'])
def get_trecks():
    """Получение всех построенных маршрутов"""
    return convert_all_object_to_json(Treck, exclude=[Treck.points])

@manager.route('/trecks/<pk>')
def get_detail_trecks(pk):
    """Получение детальной информации о построенном маршруте с id = Pk"""
    return convert_all_object_to_json(
        Treck.select().where(Treck.id == int(pk))) 

@manager.route('/trecks', methods=['POST'])
def add_trecks():
    """Создание нового маршрута из json"""
    return create_object_from_json(Treck, request.json)

@manager.route('/trecks/<pk>', methods=['DELETE'])
def del_trecks(pk):
    Treck.delete().where(Treck.id == int(pk)).execute()
    """Удаление построенного маршрута из json"""
    return jsonify({'status': 'deleted'})