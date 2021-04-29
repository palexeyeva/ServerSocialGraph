#!C:\Server\bin\Python\Python39\python.exe
# -*- coding: cp1251 -*-
print ("Content-type: text/html\n\n")
print
print ("<html><head>")
print ("")
print ("</head><body>")
print ("Hello.")
import cgi  
import vk_api 
import json
form = cgi.FieldStorage() 

val_id = int(form.getvalue("chooseID"))
print(val_id)

def captcha_handler(captcha):

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


f = open("C:/login.txt", "r")
vk_session = vk_api.VkApi(f.readline(), f.readline(), captcha_handler=captcha_handler)
print("test1")
vk_session.auth()
vk = vk_session.get_api()
print("test2")

getPersInfo = vk.users.get(user_ids = val_id, fields = 'sex, city')
print(getPersInfo)

print(getPersInfo[0]['id'])

getPersFriends = vk.friends.get(user_id = val_id, order='hints', fields = 'nickname, sex, city')
print("test3")
j = []
m = [val_id]
overAllFriends = []

for i in range(len(getPersFriends['items'])):
    j.append(getPersFriends['items'][i]['id'])
    
m.extend(j)

overAllFriends.append(m)

print("test4")

try:
    ct = getPersInfo[0]['city']['title']
except :
    ct = ''

dataFriends = {
    "people": [
        {"id": getPersInfo[0]['id'],
        "name": getPersInfo[0]['first_name'] + ' ' + getPersInfo[0]['last_name'],
        "group": getPersInfo[0]['sex'],
        "city": ct}
    ],
    "connection": overAllFriends
}
for i in range(len(getPersFriends['items'])):
    city = ""
    try: 
        city = getPersFriends['items'][i]['city']['title']
    except:   
        city = ""
    g = {"id": getPersFriends['items'][i]['id'],
    "name": getPersFriends['items'][i]['first_name'] + ' ' + getPersFriends['items'][i]['last_name'],
    "group": getPersFriends['items'][i]['sex'],
    "city": city
    }
    dataFriends["people"].append(g)
    if ('deactivated' in getPersFriends['items'][i]) == False:
        if (getPersFriends['items'][i]['is_closed'] == False):
            getCommonFriends = [getPersFriends['items'][i]['id']]
            print(getCommonFriends)
            try :
                getCommonFriends.extend(vk.friends.getMutual(source_uid = getPersInfo[0]['id'], target_uid = getPersFriends['items'][i]['id']))
                dataFriends["connection"].append(getCommonFriends)
            except: print('private')
print("test5")

f = open("data_file.json", "w", encoding = "utf-8")
json.dump(dataFriends, f, ensure_ascii=False)


print ("</body></html>")

