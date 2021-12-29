from utils import convert_all_object_to_json, create_object_from_json
from plugins.user.models import User, CodeActications
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


def send_code(user):
    code = ''.join(choices(digits, k=4))
    CodeActications.create(user=user, code=code)
    url = '/'.join(request.url.split('/')[:3])
    text = f'Пожалуйста, подтвердите вашу почту: {url}/activations/{code}'
    
    send = post(
        f'https://api.mailgun.net/v3/{getenv("MAILGUN_MAIL").split("@")[1]}/messages',
        auth=("api", getenv('MAILGUN_API_KEY')),
        data={"from": f"Hiking <{getenv('MAILGUN_MAIL')}>",
              "to": [user.email],
              "subject": 'Подверждение почты',
              "text": text}
    )
    print(send.text)


@manager.route('/login', methods=['POST'])
def login():
    json = request.json # пароль и email
    try:
        user: User = User.get(User.email == json.get('email'))
    except DoesNotExist:
        return jsonify({'error': 'Неправильный логин или пароль'})
    if user.password != md5(json['password'].encode()).hexdigest():
        return jsonify({'error': 'Неправильный логин или пароль'})
    #if not user.active:
     #   return jsonify({'error': 'Подтвердите почту'}) 

    return model_to_dict(user, backrefs=True)


@manager.route('/users', methods=['GET'])
def get_users():
    """Получение всех пользователей"""
    return convert_all_object_to_json(User)


@manager.route('/registration', methods=['POST'])
def add_users():
    """Создание нового пользователя из json"""
    json = request.json
    json['active'] = False

    if json.get('password', '') != json.pop('check_password'):
        return jsonify({'error': 'Пароли не совпадают'})

    json['password'] = md5(json['password'].encode()).hexdigest()
    
    if User.select().where(User.email == json.get('email')).exists():
        return jsonify({'error': 'Пользователь с такой почтой уже существует'})

    result = create_object_from_json(User, request.json)

    user = User.get(User.email == json.get('email'))
    send_code(user)
    
    return result


@manager.route('/activations/<code>', methods=['GET'])
def activate(code):
    try:
        code = CodeActications.get(CodeActications.code==code)
    except DoesNotExist:
        return jsonify({'error': 'Код не найден'})
    code.user.active = True
    code.user.save()
    return jsonify({'good': 'Вы успешно подтердили почту'})
