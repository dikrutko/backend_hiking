from utils import convert_all_object_to_json, create_object_from_json
from plugins.area.models import Area
from flask import request, jsonify
from plugins.core.plugin_manager import PluginManager

manager = PluginManager(None)

@manager.route('/areas', methods=['GET'])
def get_areas():
    """Получение всех районов"""
    return convert_all_object_to_json(Area)

@manager.route('/areas', methods=['POST'])
def add_areas():
    """Создание нового района из json"""
    return create_object_from_json(Area, request.json)

@manager.route('/areas/<pk>', methods=['DELETE'])
def del_areas(pk):
    Area.delete().where(Area.id == int(pk)).execute()
    """Удаление района из json"""
    return jsonify({'status': 'deleted'})

