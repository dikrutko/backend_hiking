from utils import convert_all_object_to_json, create_object_from_json
from plugins.point.models import Point
from flask import request, jsonify
from plugins.core.plugin_manager import PluginManager


manager = PluginManager(None)

@manager.route('/points', methods=['GET'])
def get_points_area():
    return convert_all_object_to_json(Point)

@manager.route('/points', methods=['POST'])
def add_points():
    return create_object_from_json(Point, request.json)

@manager.route('/points/<pk>', methods=['DELETE'])
def del_points(pk):
    Point.delete().where(Point.id == int(pk)).execute()
    return jsonify({'status': 'deleted'})
