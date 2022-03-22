from flask import jsonify, request
from plugins.core.plugin_manager import PluginManager
from plugins.treck.models import Treck
from utils import convert_all_object_to_json, create_object_from_json
from scripts.new_treck import Deikstra, lenforfway

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

@manager.route('/trecks/calc', methods=['POST'])
def calc_tarck():
    data = request.json
    fway = Deikstra(tuple(data['start']), tuple(data['stop']))
    lenght, max_tr, min_tr = lenforfway(fway, 0, int(len(fway) / 3) - 1)
    return jsonify({
        "max_tr": max_tr,
        "lenght": lenght,
        "min_tr": min_tr,
        "fway": fway,
    })
