import re
from datetime import datetime

text = "ПЕЩЕРНЫЙ ЛОГ \n \n&#128197; 4 декабря - суббота \n&#9200;Начало в 10:00 \n \nПолностью пройдем небольшую круговую тропу \"Прогулочная\" на Гремячей Гриве, зайдем в Пещерный лог, посмотрим на Монастырский грот и пещеру Карман. \n \nОБЯЗАТЕЛЬНО: правильная одежда по погоде и обувь на нескользкой подошве, чай/кофе, перекус. \n \nПротяженность - 5км \nПродолжительность: 3ч \n \n&#128204;ЗАПИСЬ по ссылке откроется в 19:00: https://travelcenter.timepad.ru/event/1858378/ \n \nБесплатно \n \n#афиша@krashiking #центрпутешественников #КрасноярскийХайкинг #твоё_время #Красноярск #ГремячаяГрива #ПещерныйЛог"

text_name1 = re.findall(r'([А-Я]{2,}\s[А-Я]{2,}\s)', text)
text_name2 = re.findall(r'[А-Я]{2,}\s[А-Я]{2,}\s[А-Я]{2,}', text)
if (text_name1 != ' ' or text_name2 != ' '):
    if (text_name1 != ' '):
        name = text_name1
    elif (text_name2 != ' '):
        name = text_name2
    print (name[0])

date_event = re.findall(r'\d{1,}\s\w+\s.\s\w+',text)
print(date_event[0])
date_split = date_event[0].split()
print(date_split)
date = date_split[0]
print(date)
mounth = date_split[1]
moun = {
            "января": '01',
            "февраля": '02',
            "марта": '03',
            "апреля": '04',
            "мая": '05',
            "июня": '06',
            "июля": '07',
            "августа": '08',
            "сентября": '09',
            "октября": '10',
            "ноября": '11',
            "декабря":'12'
        }[mounth]
print(moun)
year = datetime.now().year
print (year)
dayWeek = date_split[3]
print(dayWeek)
time_event = re.findall(r'\d{2}\:\d{2}', text)
print (time_event[0])


descript = text.split('\n')[5] + '\n' + text.split('\n')[7]
print(descript)


lenght_event = re.findall(r'[пП]ротяженность\W{1,3}\d+', text)
print(lenght_event[0])
len_num = re.findall(r'\d+', lenght_event[0])
print(len_num[0])


lenght_time_event = re.findall(r'[пП]родолжительность\W{1,3}\d+', text)
len_time_num = re.findall(r'\d+', lenght_time_event[0])
lenght_time = len_time_num[0]
# продолжительность в ч
print (lenght_time)

link_event = re.findall(r'https://\S+', text)
print(link_event[0])

price_event = re.findall(r'Бесплатно', text)
if price_event[0] == 'Бесплатно':
    price = 0
print(price)