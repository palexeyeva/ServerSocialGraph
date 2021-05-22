#!C:\Server\bin\Python\Python39\python.exe

print ("Content-type: text/html\n\n")
print
print ("<html><head>")
print ("")
print ("</head><body>")
print ("Hello.")

import cgi  
import json
import datetime
import vk_api 
import requests
import hashlib

def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

def getCountryOK(vk):
  if vk == 228: #Ямайка
    return "10415454380"
  elif vk == 1: #Россия
    return "10414533690"
  elif vk == 2: #Украина
    return "10424076448"
  elif vk == 3: #Беларусь
    return "10423319006"
  elif vk == 4: #Казахстан
    return "10415971874"
  elif vk == 5: #Азербайджан
    return "10410450732"
  elif vk == 6: #Армения
    return "10417232037"
  elif vk == 7: #Грузия
    return "10411801535"
  elif vk == 8: #Израиль
    return "10424542073"
  elif vk == 9: #США
    return "10395431810"
  elif vk == 65: #Германия
    return "10397571399"
  elif vk == 11: #Кыргызстан
    return "10405644775"
  elif vk == 12: #Латвия
    return "10405172143"
  elif vk == 13: #Литва
    return "10408982062"
  elif vk == 14: #Эстония
    return "10399393757"
  elif vk == 15: #Молдова
    return "10397135919"
  elif vk == 16: #Таджикистан
    return "10426480621"
  elif vk == 17: #Туркменистан
    return "10396721959"
  elif vk == 18: #Узбекистан
    return "10423529949"
  elif vk == 19: #Австралия
    return "10400654407"
  elif vk == 20: #Австрия
    return "10426428818"
  elif vk == 21: #Албания
    return "10410522537"
  elif vk == 22: #Алжир
    return "10419531540"
  elif vk == 23: #Американское Самоа
    return ""
  elif vk == 24: #Ангилья
    return "10395022134"
  elif vk == 25: #Ангола
    return "10400909101"
  elif vk == 26: #Андорра
    return "10396157513"
  elif vk == 27: #Антигуа и Барбуда
    return "10401935333"
  elif vk == 28: #Аргентина
    return "10401434079"
  elif vk == 29: #Аруба
    return ""
  elif vk == 30: #Афганистан
    return "10410310303"
  elif vk == 31: #Багамы
    return "10407551720"
  elif vk == 32: #Бангладеш
    return "10396352095"
  elif vk == 33: #Барбадос
    return "10411706009"
  elif vk == 34: #Бахрейн
    return "10406995556"
  elif vk == 35: #Белиз
    return "10394079228"
  elif vk == 36: #Бельгия
    return "10408272261"
  elif vk == 37: #Бенин
    return "10423428619"
  elif vk == 38: #Бермуды
    return "10414686106"
  elif vk == 39: #Болгария
    return "10393631600"
  elif vk == 40: #Боливия
    return "10409174087"
  elif vk == 235: #Бонайре, Синт-Эстатиус и Саба
    return ""
  elif vk == 41: #Босния и Герцеговина
    return "10396139862"
  elif vk == 42: #Ботсвана
    return "10401213745"
  elif vk == 43: #Бразилия
    return "10394346015"
  elif vk == 44: #Бруней
    return "10419484235"
  elif vk == 45: #Буркина-Фасо
    return "10404060904"
  elif vk == 46: #Бурунди
    return "10404374905"
  elif vk == 47: #Бутан
    return "10404540364"
  elif vk == 48: #Вануату
    return "10412870819"
  elif vk == 233: #Ватикан
    return "10411136417"
  elif vk == 49: #Великобритания
    return "10406170538"
  elif vk == 50: #Венгрия
    return "10409956165"
  elif vk == 51: #Венесуэла
    return "10396486463"
  elif vk == 52: #Виргинские острова, Великобритания
    return ""
  elif vk == 53: #Виргинские острова, США
    return ""
  elif vk == 54: #Восточный Тимор
    return ""
  elif vk == 55: #Вьетнам
    return "10415852578"
  elif vk == 56: #Габон
    return "10393450888"
  elif vk == 57: #Гаити
    return "10417683703"
  elif vk == 58: #Гайана
    return "10403255122"
  elif vk == 59: #Гамбия
    return "10399865285"
  elif vk == 60: #Гана
    return "10397676008"
  elif vk == 61: #Гваделупа
    return "10414930207"
  elif vk == 62: #Гватемала
    return "10419428643"
  elif vk == 63: #Гвинея
    return "10413226540"
  elif vk == 64: #Гвинея-Бисау
    return "10403555674"
  elif vk == 236: #Гернси
    return ""
  elif vk == 66: #Гибралтар
    return ""
  elif vk == 67: #Гондурас
    return ""
  elif vk == 68: #Гонконг
    return ""
  elif vk == 69: #Гренада
    return ""
  elif vk == 70: #Гренландия
    return ""
  elif vk == 71: #Греция
    return ""
  elif vk == 72: #Гуам
    return ""
  elif vk == 73: #Дания
    return ""
  elif vk == 237: #Джерси
    return ""
  elif vk == 231: #Джибути
    return ""
  elif vk == 74: #Доминика
    return ""
  elif vk == 75: #Доминиканская Республика
    return ""
  elif vk == 76: #Египет
    return ""
  elif vk == 77: #Замбия
    return ""
  elif vk == 78: #Западная Сахара
    return ""
  elif vk == 79: #Зимбабве
    return ""
  elif vk == 80: #Индия
    return ""
  elif vk == 81: #Индонезия
    return ""
  elif vk == 82: #Иордания
    return ""
  elif vk == 83: #Ирак
    return ""
  elif vk == 84: #Иран
    return ""
  elif vk == 85: #Ирландия
    return ""
  elif vk == 86: #Исландия
    return ""
  elif vk == 87: #Испания
    return ""
  elif vk == 88: #Италия
    return ""
  elif vk == 89: #Йемен
    return ""
  elif vk == 90: #Кабо-Верде
    return ""
  elif vk == 91: #Камбоджа
    return ""
  elif vk == 92: #Камерун
    return ""
  elif vk == 10: #Канада
    return ""
  elif vk == 93: #Катар
    return ""
  elif vk == 94: #Кения
    return ""
  elif vk == 95: #Кипр
    return ""
  elif vk == 96: #Кирибати
    return ""
  elif vk == 97: #Китай
    return ""
  elif vk == 98: #Колумбия
    return ""
  elif vk == 99: #Коморы
    return ""
  elif vk == 100: #Конго
    return ""
  elif vk == 101: #Конго, демократическая республика
    return ""
  elif vk == 102: #Коста-Рика
    return ""
  elif vk == 103: #Кот д`Ивуар
    return ""
  elif vk == 104: #Куба
    return ""
  elif vk == 105: #Кувейт
    return ""
  elif vk == 138: #Кюрасао
    return ""
  elif vk == 106: #Лаос
    return ""
  elif vk == 107: #Лесото
    return ""
  elif vk == 108: #Либерия
    return ""
  elif vk == 109: #Ливан
    return ""
  elif vk == 110: #Ливия
    return ""
  elif vk == 111: #Лихтенштейн
    return ""
  elif vk == 112: #Люксембург
    return ""
  elif vk == 113: #Маврикий
    return ""
  elif vk == 114: #Мавритания
    return ""
  elif vk == 115: #Мадагаскар
    return ""
  elif vk == 118: #Малави
    return ""
  elif vk == 119: #Малайзия
    return ""
  elif vk == 120: #Мали
    return ""
  elif vk == 121: #Мальдивы
    return ""
  elif vk == 122: #Мальта
    return ""
  elif vk == 123: #Марокко
    return ""
  elif vk == 124: #Мартиника
    return ""
  elif vk == 125: #Маршалловы Острова
    return ""
  elif vk == 126: #Мексика
    return ""
  elif vk == 127: #Микронезия, федеративные штаты
    return ""
  elif vk == 128: #Мозамбик
    return ""
  elif vk == 129: #Монако
    return ""
  elif vk == 130: #Монголия
    return ""
  elif vk == 131: #Монтсеррат
    return ""
  elif vk == 132: #Мьянма
    return ""
  elif vk == 134: #Намибия
    return ""
  elif vk == 135: #Науру
    return ""
  elif vk == 136: #Непал
    return ""
  elif vk == 137: #Нигер
    return ""
  elif vk == 138: #Нигерия
    return ""
  elif vk == 139: #Нидерланды
    return ""
  elif vk == 140: #Никарагуа
    return ""
  elif vk == 141: #Ниуэ
    return ""
  elif vk == 142: #Новая Зеландия
    return ""
  elif vk == 143: #Новая Каледония
    return ""
  elif vk == 144: #Норвегия
    return ""
  elif vk == 145: #Объединенные Арабские Эмираты
    return ""
  elif vk == 146: #Оман
    return ""
  elif vk == 147: #Остров Мэн
    return ""
  elif vk == 148: #Остров Норфолк
    return ""
  elif vk == 149: #Острова Кайман
    return ""
  elif vk == 150: #Острова Кука
    return ""
  elif vk == 151: #Острова Теркс и Кайкос
    return ""
  elif vk == 152: #Пакистан
    return ""
  elif vk == 153: #Палау
    return ""
  elif vk == 154: #Палестинская автономия
    return ""
  elif vk == 155: #Панама
    return ""
  elif vk == 156: #Папуа - Новая Гвинея
    return ""
  elif vk == 157: #Парагвай
    return ""
  elif vk == 158: #Перу
    return ""
  elif vk == 159: #Питкерн
    return ""
  elif vk == 160: #Польша
    return ""
  elif vk == 161: #Португалия
    return ""
  elif vk == 162: #Пуэрто-Рико
    return ""
  elif vk == 163: #Реюньон
    return ""
  elif vk == 164: #Руанда
    return ""
  elif vk == 165: #Румыния
    return ""
  elif vk == 166: #Сальвадор
    return ""
  elif vk == 167: #Самоа
    return ""
  elif vk == 168: #Сан-Марино
    return ""
  elif vk == 169: #Сан-Томе и Принсипи
    return ""
  elif vk == 170: #Саудовская Аравия
    return ""
  elif vk == 172: #Святая Елена
    return ""
  elif vk == 173: #Северная Корея
    return ""
  elif vk == 117: #Северная Македония
    return ""
  elif vk == 174: #Северные Марианские острова
    return ""
  elif vk == 175: #Сейшелы
    return ""
  elif vk == 176: #Сенегал
    return ""
  elif vk == 177: #Сент-Винсент и Гренадины
    return ""
  elif vk == 178: #Сент-Китс и Невис
    return ""
  elif vk == 179: #Сент-Люсия
    return ""
  elif vk == 180: #Сент-Пьер и Микелон
    return ""
  elif vk == 181: #Сербия
    return ""
  elif vk == 182: #Сингапур
    return ""
  elif vk == 234: #Синт-Мартен
    return ""
  elif vk == 183: #Сирия
    return ""
  elif vk == 184: #Словакия
    return ""
  elif vk == 185: #Словения
    return ""
  elif vk == 186: #Соломоновы Острова
    return ""
  elif vk == 187: #Сомали
    return ""
  elif vk == 188: #Судан
    return ""
  elif vk == 189: #Суринам
    return ""
  elif vk == 190: #Сьерра-Леоне
    return ""
  elif vk == 191: #Таиланд
    return ""
  elif vk == 192: #Тайвань
    return ""
  elif vk == 193: #Танзания
    return ""
  elif vk == 194: #Того
    return ""
  elif vk == 195: #Токелау
    return ""
  elif vk == 196: #Тонга
    return ""
  elif vk == 197: #Тринидад и Тобаго
    return ""
  elif vk == 198: #Тувалу
    return ""
  elif vk == 199: #Тунис
    return ""
  elif vk == 200: #Турция
    return ""
  elif vk == 201: #Уганда
    return ""
  elif vk == 202: #Уоллис и Футуна
    return ""
  elif vk == 203: #Уругвай
    return ""
  elif vk == 204: #Фарерские острова
    return ""
  elif vk == 205: #Фиджи
    return ""
  elif vk == 206: #Филиппины
    return ""
  elif vk == 207: #Финляндия
    return ""
  elif vk == 208: #Фолклендские острова
    return ""
  elif vk == 209: #Франция
    return ""
  elif vk == 210: #Французская Гвиана
    return ""
  elif vk == 211: #Французская Полинезия
    return ""
  elif vk == 212: #Хорватия
    return ""
  elif vk == 213: #Центральноафриканская Республика
    return ""
  elif vk == 214: #Чад
    return ""
  elif vk == 230: #Черногория
    return ""
  elif vk == 215: #Чехия
    return ""
  elif vk == 216: #Чили
    return ""
  elif vk == 217: #Швейцария
    return ""
  elif vk == 218: #Швеция
    return ""
  elif vk == 219: #Шпицберген и Ян Майен
    return ""
  elif vk == 220: #Шри-Ланка
    return ""
  elif vk == 221: #Эквадор
    return ""
  elif vk == 222: #Экваториальная Гвинея
    return ""
  elif vk == 223: #Эритрея
    return ""
  elif vk == 171: #Эсватини
    return ""
  elif vk == 224: #Эфиопия
    return ""
  elif vk == 226: #Южная Корея
    return ""
  elif vk == 227: #Южно-Африканская Республика
    return ""
  elif vk == 232: #Южный Судан
    return ""
  elif vk == 229: #Япония
    return ""
  else: return ""

f = open("C:/login.txt", "r")
vk_session = vk_api.VkApi(f.readline(), f.readline(), captcha_handler=captcha_handler)
vk_session.auth()
vk = vk_session.get_api()

#Загрузка данных из формы и их форматирование
form = cgi.FieldStorage() 
name = form.getvalue("name")
surName = form.getvalue("surName")
bdate = form.getvalue("bdate")
try:
    ageFrom = form.getvalue("ageFrom")
    ageTo = form.getvalue("ageTo")
    job = form.getvalue("job")
except: 
    ageFrom = ""
    ageTo = ""
    job = ""
if form.getvalue("bdate") != None:
    byear = bdate[0:4]
    bmonth = bdate[5:7]
    bday = bdate[8:10]
else:
    bdate = None
    bday = None
    bmonth = None
    byear = None
sex = form.getvalue("user_sex")
country = form.getvalue("country")
if form.getvalue("city") and country:
    city = vk.database.getCities(country_id = country, q= form.getvalue("city"))["items"][0]["id"]
else:
    city = None

#ВКонтакте

searchResults=vk.users.search(q = name + ' ' + surName,  
birth_day = bday, birth_month = bmonth,  birth_year = byear, 
sex = sex,  country = country, city = city, age_from = ageFrom, 
age_To = ageTo, company = job, count = 100, fields='bdate, city, photo_200_orig, screen_name, is_closed')

returnResults = []

for i in range(len(searchResults['items'])):
    if searchResults['items'][i]['is_closed'] == False:
        g = []
        id = ''
        name = ''
        surname = ''
        bdate = ''
        href = ''
        photo = ''
        city = ''
        id = searchResults['items'][i]['id']    
        name = searchResults['items'][i]['first_name']    
        surname = searchResults['items'][i]['last_name'] 
        try:
            bdate = searchResults['items'][i]['bdate']
        except: 
            bdate = '' 
        href = 'https://vk.com/' + searchResults['items'][i]['screen_name']    
        try: 
            photo = searchResults['items'][i]['photo_200_orig']
        except: 
            photo = ''    
        try: 
            city = searchResults['items'][i]['city']['title']
        except: 
            city = ''    
        g = [name, surname, bdate, href, photo, city, id]
        returnResults.append(g)

f = open('res.txt', 'w', encoding = "utf-8")
for item in returnResults:
    f.write("%s;%s;%s;%s;%s;%s;%s\n" % (item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
f.close


#Одноклассники 

accToken = 'access_token=tkn1wp2gC0422oPUo4bG62J9tVcqEcv4uc9LRSwdSlm4bTdmnNbA4jYKQBokNkAPuvtCH'
appKey = 'application_key=CBLFAQJGDIHBABABA'
appSec = '8825c8ac78ab7523c0376d438aea9ba1'

headers = {'Content-Type':'application/json',
'Cookie': 'bci=5950650924462897331; _statid=4d1a418c-731e-4c3e-bcdf-7791d79340a2; viewport=824; _userIds=""; _suserIds=""; TZ=6; _flashVersion=0; nbp=; msg_conf=2468555756792551; cudr=0; klos=0; LASTSRV=ok.ru; CDN=; AUTHCODE=Jay_C25y0dgJpfLEaZ16qPQxwXyrcQxCD0XSqsRewIT75xx-YSebhWuHjwQeSnnl0j3dlrekAhtTZ5ORmnagEQGW5XRO0ewWPV8Cve8Ui4-5hUvT6CDTpt5K_RPo8QFFp1EtmLNSwtk0UGE_3; JSESSIONID=aea0980ba373a5d38160db32767149118a35ce44f2e573f6.100a24b6; TZD=6.7430; TD=7430'}  

json = {
  "id": 72,
  "parameters": {
    "query": "",
    "filters": {
      "st.cmd": "searchResult",
      "st.mode": "Users",
      "st.query": "",
      "st.grmode": "Groups"
    },
    "chunk": {
      "firstIndex": 0,
      "offset": 0
    },
    "prefetch": False
  }
}

if sex == 1:
    sex = "f"
elif sex == 2:
    sex = "m"
else: sex = None

json["parameters"]["query"] = name + " " + surName
json["parameters"]["filters"]["st.query"] = name + " " + surName
if bday!=None or bmonth!=None or bday!=None:
  if bday!=None:
    json["parameters"]["filters"]["st.bthDay"] = str(bday)
  if bmonth!=None:
    json["parameters"]["filters"]["st.bthMonth"] = str(bmonth)
  if byear!=None:
    json["parameters"]["filters"]["st.bthYear"] = str(byear)
elif ageTo!=None or ageFrom!=None:
  if ageTo!=None:
    json["parameters"]["filters"]["st.tillAge"] = str(ageTo)
  if ageFrom!=None:
    json["parameters"]["filters"]["st.fromAge"] = str(ageFrom)
if country!=None:
  json["parameters"]["filters"]["st.country"] = str(getCountryOK(country))
if city!=None:
  json["parameters"]["filters"]["st.location"] = form.getvalue("city")


f = open('resOK.txt', 'w', encoding = "utf-8")
f.write("")
f.close
firstIndex = 0
while firstIndex <= 80:
  json["parameters"]["chunk"]["firstIndex"] = firstIndex
  r = requests.post('https://ok.ru/web-api/v2/search/portal', json=json, headers=headers)
  r=r.json()
  firstIndex = firstIndex + 20

  try:
    l = len(r['result']['users']['values']['results'])
  except: l = 0
  returnResults = []
  if l != 0: 
    for i in range(l):
      g = []
      id = ''
      name = ''
      surname = ''
      age = ''
      href = ''
      photo = ''
      location = ''
      href = 'https://ok.ru' + r['result']['users']['values']['results'][i]['user']['info']['shortLink']
      name = r['result']['users']['values']['results'][i]['user']['info']['firstName']
      surname = r['result']['users']['values']['results'][i]['user']['info']['lastName']
      id = r['result']['users']['values']['results'][i]['user']['info']['uid']
      sigToMd = appKey + 'fields=BIRTHDAY,pic_fullformat=jsonmethod=users.getInfouids=' + id + appSec
      hash_object = hashlib.md5(sigToMd.encode())
      urlOKgetInfo = 'https://api.ok.ru/fb.do?' + appKey + '&fields=BIRTHDAY%2Cpic_full&format=json&method=users.getInfo&uids=' + id + '&sig=' + hash_object.hexdigest() + '&' + accToken  
      searchUserOK = requests.post(urlOKgetInfo)
      sk = searchUserOK.json()
      bdate = sk[0]['birthday']
      try:
        city = r['result']['users']['values']['results'][i]['user']['location']  
      except:
        city = ''
      try:
        photo = sk[0]['pic_full']
      except:
        photo = ''
        
      g = [name, surname, bdate, href, photo, city, id]
      returnResults.append(g)

    f = open('resOK.txt', 'a', encoding = "utf-8")
    for item in returnResults:
      f.write("%s;%s;%s;%s;%s;%s;%s\n" % (item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
    f.close
  else:
    f = open('resOK.txt', 'a', encoding = "utf-8")
    f.write("")
    f.close

print ("</body></html>")