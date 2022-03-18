from utils import convert_all_object_to_json, create_object_from_json
from plugins.user.models import User
from flask import request, jsonify
from plugins.core.plugin_manager import PluginManager
from hashlib import md5
from playhouse.shortcuts import model_to_dict
from string import digits
from random import choices
from peewee import DoesNotExist
from requests import post
from os import getenv


manager = PluginManager(None)


@manager.route('/login', methods=['POST'])
def login():
    json = request.json # пароль и email
    try:
        user: User = User.get(User.email == json.get('email'))
    except DoesNotExist:
        return jsonify({'error': 'Неправильный логин или пароль'})
    if user.password != md5(json['password'].encode()).hexdigest():
        return jsonify({'error': 'Неправильный логин или пароль'})
    return model_to_dict(user, backrefs=True)


@manager.route('/users', methods=['GET'])
def get_users():
    """Получение всех пользователей"""
    return convert_all_object_to_json(User)


@manager.route('/registration', methods=['POST'])
def add_users():
    """Создание нового пользователя из json"""
    json = request.json

    if json.get('password', '') != json.pop('check_password'):
        return jsonify({'error': 'Пароли не совпадают'})

    json['password'] = md5(json['password'].encode()).hexdigest()
    
    if User.select().where(User.email == json.get('email')).exists():
        return jsonify({'error': 'Пользователь с такой почтой уже существует'})

    result = create_object_from_json(User, request.json)

    user = User.get(User.email == json.get('email'))
    send_code(user)
    
    return result