from flask import jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model
from peewee import IntegrityError


def convert_all_object_to_json(obj, **kwargs) -> list:
    result = []

    for element in obj.select():
        result.append(model_to_dict(element, backrefs=True, **kwargs))
    
    return jsonify(result)


def create_object_from_json(obj, json):
    """Создание новой новости из json"""

    element = dict_to_model(obj, json)

    try:
        element.save()
        element = obj.select().where(obj.id==element.id).get()
    except IntegrityError as e:
        # Отлавливаем ошибку, если что-то пошло не так
        return jsonify({'error': str(e)})

    return jsonify(model_to_dict(element))
