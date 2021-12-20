from utils import convert_all_object_to_json, create_object_from_json
from plugins.team.models import Team
from flask import request, jsonify
from plugins.core.plugin_manager import PluginManager


manager = PluginManager(None)


@manager.route('/team', methods=['GET'])
def get_team():
    """Получение всех людей из командв"""
    return convert_all_object_to_json(Team)

@manager.route('/team', methods=['POST'])
def add_team():
    """Добавление нового человека в команду из json"""
    return create_object_from_json(Team, request.json)

@manager.route('/team/<pk>', methods=['DELETE'])
def del_team(pk):
    Team.delete().where(Team.id == int(pk)).execute()
    """Удаление человека из команды из json"""
    return jsonify({'status': 'deleted'})
