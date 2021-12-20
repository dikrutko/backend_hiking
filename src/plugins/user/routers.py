from utils import convert_all_object_to_json, create_object_from_json
from plugins.user.models import User
from flask import request, jsonify
from plugins.core.plugin_manager import PluginManager


manager = PluginManager(None)


@manager.route('/users', methods=['GET'])
def get_users():
    """Получение всех районов"""
    return convert_all_object_to_json(User)


@manager.route('/users', methods=['POST'])
def add_users():
    """Создание нового района из json"""
    return create_object_from_json(User, request.json)


@manager.route('/users/<pk>', methods=['DELETE'])
def del_users(pk):
    User.delete().where(User.id == int(pk)).execute()
    """Удаление района из json"""
    return jsonify({'status': 'deleted'})
