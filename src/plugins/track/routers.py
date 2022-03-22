from flask import jsonify, request
from plugins.core.plugin_manager import PluginManager
from plugins.track.models import Track
from utils import convert_all_object_to_json, create_object_from_json
from .scripts.new_track import Deikstra, lenforfway

manager = PluginManager(None)

@manager.route('/tracks', methods=['GET'])
def get_tracks():
    """Получение всех построенных маршрутов"""
    return convert_all_object_to_json(Track, exclude=[Track.points])

@manager.route('/tracks/<pk>')
def get_detail_tracks(pk):
    """Получение детальной информации о построенном маршруте с id = Pk"""
    return convert_all_object_to_json(
        Track.select().where(Track.id == int(pk))) 

@manager.route('/tracks', methods=['POST'])
def add_tracks():
    """Создание нового маршрута из json"""
    return create_object_from_json(Track, request.json)

@manager.route('/tracks/<pk>', methods=['DELETE'])
def del_tracks(pk):
    Track.delete().where(Track.id == int(pk)).execute()
    """Удаление построенного маршрута из json"""
    return jsonify({'status': 'deleted'})

@manager.route('/tracks/calc', methods=['POST'])
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
