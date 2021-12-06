from flask import Flask, request, jsonify
from flask.json import dumps
import models
from playhouse.shortcuts import model_to_dict, dict_to_model
from peewee import DateTimeField, IntegrityError
from utils import convert_all_object_to_json, create_object_from_json
from datetime import datetime
from scripts.parser_coords_on_map import pars_coords
import re


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/news', methods=['GET'])
def get_news():
    """Получение всех новостей"""
    return convert_all_object_to_json(models.News)

@app.route('/news', methods=['POST'])
def add_news():
    """Создание новой новости из json"""
    return create_object_from_json(models.News, request.json)

@app.route('/news/<pk>', methods=['DELETE'])
def del_news(pk):
    models.News.delete().where(models.News.id == int(pk)).execute()
    """Удаление новости из json"""
    return jsonify({'status': 'deleted'})


@app.route('/coords/<name>', methods=['GET'])
def get_coords_from_map(name):
    return pars_coords(name)


@app.route('/news_vk', methods=['POST'])
def load_news_from_vk():
    #{ "type": "confirmation", "group_id": 126669581 }
    #5aa2565d
    if not request.json:
        return 'hello'
    if request.json.get('type') == 'confirmation':
        return '5aa2565d'
    if request.json.get('type') == 'wall_post_new':
        # TODO: написать парсер
        text = request.json['object']['text']
        name =""
        datetime =""
        description =""
        lenght =""
        lenght_time =""
        link =""
        price =""
        picture =""
        # Парсим информацию 
        # Достаем название
        text_name1 = re.findall(r'([А-Я]{2,}\s[А-Я]{2,}\s)', text)
        text_name2 = re.findall(r'[А-Я]{2,}\s[А-Я]{2,}\s[А-Я]{2,}', text)
        if (text_name1 != ' ' or text_name2 != ' '):
            if (text_name1 != ' '):
                name = text_name1
            elif (text_name2 != ' '):
                name = text_name2
            name = name[0]
        #name = text.split('\n')[0]
        
        # Достаем дату и время
        date_event = re.findall(r'\d{1,}\s\w+\s.\s\w+',text)
        date_split = date_event[0].split()
        day = date_split[0]
        mounth = date_split[1]
        if (mounth == "января"):
            moun = "01"
        elif (mounth == "февраля"):
            moun = "02"
        elif (mounth == "марта"):
            moun = "03"
        elif (mounth == "апреля"):
            moun = "04"
        elif (mounth == "мая"):
            moun = "05"
        elif (mounth == "июня"):
            moun = "06"
        elif (mounth == "июля"):
            moun = "07"
        elif (mounth == "августа"):
            moun = "08"
        elif (mounth == "сентября"):
            moun = "09"
        elif (mounth == "октября"):
            moun = "10"
        elif (mounth == "ноября"):
            moun = "11"
        elif (mounth == "декабря"):
            moun = "12"
        year = DateTimeField.now().year
        time_event = re.findall(r'\d{2}\:\d{2}', text)
        time = time_event[0]
        datetime = str(year)+'-'+str(moun)+'-'+str(day)+' '+str(time)+':00'

        # Описание
        description = text.split('\n')[5] + '\n' + text.split('\n')[7]

        # Длину маршрута (протяженность), км
        lenght_event = re.findall(r'\w{13}\:\s\d{1,}\w{2}', text)
        len_split = lenght_event[0].split()
        len_num = re.findall(r'\d{1,}', len_split[1])
        lenght = len_num[0]

        # Продолжительность, ч
        lenght_time_event = re.findall(r'\w{17}\:\s\d{1,}\w{1}', text)
        len_time_split = lenght_time_event[0].split()
        len_time_num = re.findall(r'\d{1,}', len_time_split[1])
        lenght_time = len_time_num[0]

        # Ссылку на регистриацию
        link_event = re.findall(r'https://\S+', text)
        link = link_event[0]

        # Цену
        price_event = re.findall(r'Бесплатно', text)
        if price_event[0] == 'Бесплатно':
            price = 0

        jsonArray1 = request.json['attachments']
        for i in jsonArray1:
            # Вытаскиваем картинку из поста
            if jsonArray1[i].get('type') == 'photo':
                jsonArray2 = request.json['sizes']
                for j in jsonArray2:
                    if jsonArray2[j].get('type') == 'x':
                        picture = jsonArray2[j].get('url')
            # вытаскиваем ссылку на регистрацию
            if jsonArray1[i].get('type') == 'link':
                link = jsonArray1[i].get('url')
        if (name != "" and datetime != "" and description != "" and lenght != "" and lenght_time != "" and link != "" and price != "" and picture != ""):
            models.News(
                name=name,
                datetime=datetime,
                description=description,
                lenght=lenght,
                lenght_time=lenght_time,
                link_on_registration = link,
                price = price,
                picture = picture,
            ).save()

        return 'ok'
    return 'hello'
###################################################################################
@app.route('/news_vk', methods=['GET'])
def get_news_from_vk():
    """Получение всех новостей из вк"""
    return convert_all_object_to_json(models.News)
###################################################################################

@app.route('/areas', methods=['GET'])
def get_areas():
    """Получение всех районов"""
    return convert_all_object_to_json(models.Area)

@app.route('/areas', methods=['POST'])
def add_areas():
    """Создание нового района из json"""
    return create_object_from_json(models.Area, request.json)

@app.route('/areas/<pk>', methods=['DELETE'])
def del_areas(pk):
    models.Area.delete().where(models.Area.id == int(pk)).execute()
    """Удаление района из json"""
    return jsonify({'status': 'deleted'})


@app.route('/routes', methods=['GET'])
def get_routes():
    """Получение всех маршрутов"""
    return convert_all_object_to_json(models.Route, exclude=[models.Route.area])

@app.route('/routes/<pk>')
def get_detail_routes(pk):
    """Получение детальной информации о маршруте с id = Pk"""
    return convert_all_object_to_json(
        models.Route.select().where(models.Route.id == int(pk))) 

@app.route('/routes', methods=['POST'])
def add_routes():
    """Создание нового маршрута из json"""
    return create_object_from_json(models.Route, request.json)

@app.route('/routes/<pk>', methods=['DELETE'])
def del_routes(pk):
    models.Route.delete().where(models.Route.id == int(pk)).execute()
    """Удаление маршрута из json"""
    return jsonify({'status': 'deleted'})


@app.route('/places', methods=['GET'])
def get_places():
    """Получение всех маршрутов"""
    return convert_all_object_to_json(models.Place, exclude=[models.Place.area])

@app.route('/places/<pk>')
def get_detail_places(pk):
    """Получение детальной информации о маршруте с id = Pk"""
    return convert_all_object_to_json(
        models.Place.select().where(models.Place.id == int(pk))) 

@app.route('/places', methods=['POST'])
def add_places():
    """Создание нового маршрута из json"""
    return create_object_from_json(models.Place, request.json)

@app.route('/places/<pk>', methods=['DELETE'])
def del_places(pk):
    models.Place.delete().where(models.Place.id == int(pk)).execute()
    """Удаление маршрута из json"""
    return jsonify({'status': 'deleted'})


@app.route('/team', methods=['GET'])
def get_team():
    """Получение всех людей из командв"""
    return convert_all_object_to_json(models.Team)

@app.route('/team', methods=['POST'])
def add_team():
    """Добавление нового человека в команду из json"""
    return create_object_from_json(models.Team, request.json)

@app.route('/team/<pk>', methods=['DELETE'])
def del_team(pk):
    models.Team.delete().where(models.Team.id == int(pk)).execute()
    """Удаление человека из команды из json"""
    return jsonify({'status': 'deleted'})


if __name__ == '__main__':
    app.run(debug=True)
