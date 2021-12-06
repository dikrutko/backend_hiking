import re
from datetime import datetime

text = "ПЕЩЕРНЫЙ ЛОГ \n \n&#128197; 4 декабря - суббота \n&#9200;Начало в 10:00 \n \nПолностью пройдем небольшую круговую тропу \"Прогулочная\" на Гремячей Гриве, зайдем в Пещерный лог, посмотрим на Монастырский грот и пещеру Карман. \n \nОБЯЗАТЕЛЬНО: правильная одежда по погоде и обувь на нескользкой подошве, чай/кофе, перекус. \n \nПротяженность: 5км \nПродолжительность: 3ч \n \n&#128204;ЗАПИСЬ по ссылке откроется в 19:00: https://travelcenter.timepad.ru/event/1858378/ \n \nБесплатно \n \n#афиша@krashiking #центрпутешественников #КрасноярскийХайкинг #твоё_время #Красноярск #ГремячаяГрива #ПещерныйЛог"

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
print(moun)
year = datetime.now().year
print (year)
dayWeek = date_split[3]
print(dayWeek)
time_event = re.findall(r'\d{2}\:\d{2}', text)
print (time_event[0])


descript = text.split('\n')[5] + '\n' + text.split('\n')[7]
print(descript)


lenght_event = re.findall(r'\w{13}\:\s\d{1,}\w{2}', text)
len_split = lenght_event[0].split()
len_num = re.findall(r'\d{1,}', len_split[1])
# протяженность в км
print (len_num[0])

lenght_time_event = re.findall(r'\w{17}\:\s\d{1,}\w{1}', text)
len_time_split = lenght_time_event[0].split()
len_time_num = re.findall(r'\d{1,}', len_time_split[1])
# продолжительность в ч
print (len_time_num[0])

link_event = re.findall(r'https://\S+', text)
print(link_event[0])

price_event = re.findall(r'Бесплатно', text)
if price_event[0] == 'Бесплатно':
    price = 0
print(price)