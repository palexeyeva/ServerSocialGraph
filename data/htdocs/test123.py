#!C:\Server\bin\Python\Python39\python.exe


import vk_api # Импорт API
import datetime
import requests
from ok_api import OkApi
import hashlib

# mystring ='HELLO'
# hash_object = hashlib.md5(mystring.encode())
# print(hash_object.hexdigest())

def getCountryOK(vk):
  if vk == 228: #ямайка
    return "10415454380"
  elif vk == 1: #Россия
    return "10414533690"
  elif vk == 2: #Украина
    return "10424076448"

headers = {'Content-Type':'application/json','Cookie': 'bci=5950650924462897331; _statid=4d1a418c-731e-4c3e-bcdf-7791d79340a2; viewport=824; _userIds=""; _suserIds=""; TZ=6; _flashVersion=0; nbp=; msg_conf=2468555756792551; cudr=0; klos=0; LASTSRV=ok.ru; CDN=; AUTHCODE=Jay_C25y0dgJpfLEaZ16qPQxwXyrcQxCD0XSqsRewIT75xx-YSebhWuHjwQeSnnl0j3dlrekAhtTZ5ORmnagEQGW5XRO0ewWPV8Cve8Ui4-5hUvT6CDTpt5K_RPo8QFFp1EtmLNSwtk0UGE_3; JSESSIONID=aea0980ba373a5d38160db32767149118a35ce44f2e573f6.100a24b6; TZD=6.7430; TD=7430'}  
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
name = "Анастасия"
surName = "Шевченко"
ageFrom = None#"16"
ageTo = None#"40"
bday = "7"
bmonth = "5"
byear = None#"1999"
sex = "f"
country = 1
city = "Москва"
json["parameters"]["query"] = name + " " + surName
json["parameters"]["filters"]["st.query"] = name + " " + surName
if bday!=None or bmonth!=None or bday!=None:
  if bday!=None:
    json["parameters"]["filters"]["st.bthDay"] = bday
  if bmonth!=None:
    json["parameters"]["filters"]["st.bthMonth"] = bmonth
  if byear!=None:
    json["parameters"]["filters"]["st.bthYear"] = byear
elif ageTo!=None or ageFrom!=None:
  if ageTo!=None:
    json["parameters"]["filters"]["st.tillAge"] = ageTo
  if ageFrom!=None:
    json["parameters"]["filters"]["st.fromAge"] = ageFrom
if country!=None:
  json["parameters"]["filters"]["st.country"] = getCountryOK(country)
if city!=None:
  json["parameters"]["filters"]["st.location"] = city
#print(json)

r = requests.post('https://ok.ru/web-api/v2/search/portal', json=json, headers=headers)
r=r.json()
print(r)

ok = OkApi(access_token='tkn1wp2gC0422oPUo4bG62J9tVcqEcv4uc9LRSwdSlm4bTdmnNbA4jYKQBokNkAPuvtCH',
application_key='CBLFAQJGDIHBABABA',
application_secret_key='8825c8ac78ab7523c0376d438aea9ba1')

accToken = 'access_token=tkn1wp2gC0422oPUo4bG62J9tVcqEcv4uc9LRSwdSlm4bTdmnNbA4jYKQBokNkAPuvtCH'
appKey = 'application_key=CBLFAQJGDIHBABABA'
appSec = '8825c8ac78ab7523c0376d438aea9ba1'

# sigToMd = appKey + 'fields=BIRTHDAYformat=jsonmethod=users.getInfouids=' + id + appSec

# tr = requests.post('https://api.ok.ru/fb.do?application_key=CBLFAQJGDIHBABABA&fields=BIRTHDAY&format=json&method=users.getInfo&uids=579017451680&sig=1cdd93a084bcda0ea85aaf5c6037999a&access_token=tkn1wp2gC0422oPUo4bG62J9tVcqEcv4uc9LRSwdSlm4bTdmnNbA4jYKQBokNkAPuvtCH')
# print((tr.json()))

returnResults = []
for i in range(len(r['result']['users']['values']['results'])):
  g = []
  id = ''
  name = ''
  surname = ''
  age = ''
  href = ''
  photo = ''
  city = ''
  href = 'https://ok.ru' + r['result']['users']['values']['results'][i]['user']['info']['shortLink']
  name = r['result']['users']['values']['results'][i]['user']['info']['firstName']
  surname = r['result']['users']['values']['results'][i]['user']['info']['lastName']
  id = r['result']['users']['values']['results'][i]['user']['info']['uid']
  sigToMd = appKey + 'fields=BIRTHDAYformat=jsonmethod=users.getInfouids=' + id + appSec
  hash_object = hashlib.md5(sigToMd.encode())
  urlOKgetInfo = 'https://api.ok.ru/fb.do?' + appKey + '&fields=BIRTHDAY&format=json&method=users.getInfo&uids=' + id + '&sig=' + hash_object.hexdigest() + '&' + accToken  
  searchUserOK = requests.post(urlOKgetInfo)
  sk = searchUserOK.json()
  bd = sk[0]['birthday']
  try:
    age = r['result']['users']['values']['results'][i]['user']['info']['age'] 
  except:
    age=''
  try:
    city = r['result']['users']['values']['results'][i]['user']['location']  
  except:
    city = ''
  
  g = [name, surname, age, href, photo, city, id]

  #print(g)
  returnResults.append(g)
# print(returnResults)
  





'''
f = open("C:\login.txt", "r")
vk_session = vk_api.VkApi(f.readline(), f.readline())
vk_session.auth()
vk = vk_session.get_api()

name = 'Диляра'
surName = 'Минниханова'
bdate =  datetime.date(1999, 5, 5)
bday = int(bdate.day)
bmonth = int(bdate.month)
byear = int(bdate.year)
country = 1
city = vk.database.getCities(country_id = country, q= "Москва")["items"][0]["id"]
sex = 0

#print(vk.database.getCities(country_id = 1, q= "москва")["items"][0]["title"])
j=vk.users.search(q = name + ' ' + surName,  birth_day = bday, birth_month = bmonth,  birth_year = byear, sex = sex,  country = country, city = city, count = 100, fields='bdate, city, photo_50')
#j=vk.users.search(q = user_name + ' ' + user_surname,birth_day = user_bd.day, birth_month = user_bd.month, birth_year = user_bd.year, country = 1, city = vk.database.getCities(country_id = 1, q= "москва")["items"][0]["id"], count = 100, fields='bdate, city, photo_50')

print(j) # вывод полученных данных
#, birth_day = user_bd.day, birth_month = user_bd.month, birth_year = user_bd.year

print(j["items"][0]["city"]["title"])


#c = vk.database.getCities(country_id = 1)
#print (c)

#countryID = 1
#q = 'мо'
#city = vk.database.getCities(country_id = countryID, q= q)
#print (city)
#for c in city:
#  print(str(c.title) + ' с кодом ' + str(c.id) + '\n')
'''