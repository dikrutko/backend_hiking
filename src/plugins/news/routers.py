from utils import convert_all_object_to_json, create_object_from_json
from plugins.news.models import News
from flask import request, jsonify
from plugins.core.plugin_manager import PluginManager
import re
from scripts.parser_coords_on_map import pars_coords
from datetime import datetime



manager = PluginManager(None)

@manager.route('/coords/<name>', methods=['GET'])
def get_coords_from_map(name):
    return pars_coords(name)


@manager.route('/news_vk', methods=['POST'])
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
        _datetime =""
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
        moun = {
            "янв": '01',
            "фев": '02',
            "мар": '03',
            "апр": '04',
            "мая": '05',
            "июн": '06',
            "июл": '07',
            "авг": '08',
            "сен": '09',
            "окт": '10',
            "ноя": '11',
            "дек": '12'
        }[mounth[:3]]
        year = datetime.now().year
        time_event = re.findall(r'\d{2}\:\d{2}', text)
        time = time_event[0]
        _datetime = str(year)+'-'+str(moun)+'-'+str(day)+' '+str(time)+':00'

        # Описание
        description = text.split('\n')[5] + '\n' + text.split('\n')[7]

        # Длину маршрута (протяженность), км
        lenght_event = re.findall(r'[пП]ротяж[её]нность\W{1,3}\d+', text)
        len_num = re.findall(r'\d+', lenght_event[0])
        lenght = len_num[0]

        # Продолжительность, ч
        lenght_time_event = re.findall(r'[пП]родолжительность\W{1,3}\d+', text)
        len_time_num = re.findall(r'\d+', lenght_time_event[0])
        lenght_time = len_time_num[0]

        # Ссылку на регистриацию
        link_event = re.findall(r'https://\S+', text)
        link = link_event[0]

        # Цену
        price_event = re.findall(r'Бесплатно', text)
        if price_event[0] == 'Бесплатно':
            price = 0

        if attachments := request.json['object'].get('attachments'):
            for attach in attachments:
                if attach['type'] != 'photo':
                    continue
                photo = attach['photo']
                for size in photo['sizes']:
                    if size['type'] != 'x':
                        continue
                    picture = size['url']
        if name and _datetime and description and lenght and lenght_time and link and price and picture:
            News(
                name=name,
                datetime=_datetime,
                description=description,
                lenght=lenght,
                lenght_time=lenght_time,
                link_on_registration = link,
                price = price,
                picture = picture,
            ).save()

        return 'ok'
    return 'hello'