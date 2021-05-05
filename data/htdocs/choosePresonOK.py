#!C:\Server\bin\Python\Python39\python.exe

print ("Content-type: text/html\n\n")
print
print ("<html><head>")
print ("")
print ("</head><body>")
print ("Hello.")
import cgi  
import vk_api 
import json
import requests
import hashlib

print('test2')

form = cgi.FieldStorage() 
val_id = str(form.getvalue("chooseID"))
# print(val_id)
# val_id = str(564772633586)


accToken = 'access_token=tkn1wp2gC0422oPUo4bG62J9tVcqEcv4uc9LRSwdSlm4bTdmnNbA4jYKQBokNkAPuvtCH'
appKey = 'application_key=CBLFAQJGDIHBABABA'
appSec = '8825c8ac78ab7523c0376d438aea9ba1'

sigToMd = appKey + 'fields=gender,location,first_name,last_nameformat=jsonmethod=users.getInfouids=' + val_id + appSec
hash_object = hashlib.md5(sigToMd.encode())
urlOKgetInfo = 'https://api.ok.ru/fb.do?' + appKey + '&fields=gender%2Clocation%2Cfirst_name%2Clast_name&format=json&method=users.getInfo&uids=' + val_id + '&sig=' + hash_object.hexdigest() + '&' + accToken  
searchUserOK = requests.post(urlOKgetInfo)
sk = searchUserOK.json()
# print(sk)

sigToFriends = appKey + 'fid='+ sk[0]['uid'] + 'format=jsonmethod=friends.get' + appSec
hash_objectFriend = hashlib.md5(sigToFriends.encode())
urlOKgetFriend = 'https://api.ok.ru/fb.do?' + appKey + '&fid=' + sk[0]['uid'] + '&format=json&method=friends.get' + '&sig=' + hash_objectFriend.hexdigest() + '&' + accToken  
searchFriendOK = requests.post(urlOKgetFriend)
sFr = searchFriendOK.json()
# print(sFr)

j = []
m = [sk[0]['uid']]
overAllFriends = []

for i in range(len(sFr)):
    j.append(sFr[i])
    
m.extend(j)

overAllFriends.append(m)

# print(overAllFriends)


if sk[0]['gender'] == "female":
    sex = 1
elif sk[0]['gender'] == "male":
    sex = 2
else: sex = 0

dataFriends = {
    "people": [
        {"id": sk[0]['uid'],
        "name": sk[0]['first_name'] + ' ' + sk[0]['last_name'],
        "group": sex,
        "city": sk[0]['location']['city']}
    ],
    "connection": overAllFriends
}
# print(dataFriends)


for i in range(len(sFr)):
    # print("test2")
    sigToMdF = appKey + 'fields=gender,location,first_name,last_nameformat=jsonmethod=users.getInfouids=' + str(sFr[i]) + appSec
    hash_objectF = hashlib.md5(sigToMdF.encode())
    urlOKgetInfoF = 'https://api.ok.ru/fb.do?' + appKey + '&fields=gender%2Clocation%2Cfirst_name%2Clast_name&format=json&method=users.getInfo&uids=' + str(sFr[i]) + '&sig=' + hash_objectF.hexdigest() + '&' + accToken  
    searchUserOKF = requests.post(urlOKgetInfoF)
    # print("test3")
    infoF = searchUserOKF.json()
    # print(infoF)
    city = ""
    try: 
        city = infoF[0]['location']['city']
    except:   
        city = ""

    if infoF[0]['gender'] == "female":
        sex = 1
    elif infoF[0]['gender'] == "male":
        sex = 2
    else: sex = 0
    # print("test4")
    g = {"id": infoF[0]['uid'],
    "name": infoF[0]['first_name'] + ' ' + infoF[0]['last_name'],
    "group": sex,
    "city": city
    }
    dataFriends["people"].append(g)
    findF = [infoF[0]['uid']]
    # print(findF)
    sigToFriends = appKey + 'fid='+ infoF[0]['uid'] + 'format=jsonmethod=friends.get' + appSec
    hash_objectFriend = hashlib.md5(sigToFriends.encode())
    urlOKgetFriend = 'https://api.ok.ru/fb.do?' + appKey + '&fid=' + infoF[0]['uid'] + '&format=json&method=friends.get' + '&sig=' + hash_objectFriend.hexdigest() + '&' + accToken  
    searchFriendOK = requests.post(urlOKgetFriend)
    ff = searchFriendOK.json()
    # print(ff)
    if ("error_code" in ff) == False:
        print("------", ff)
        print(len(ff))
        # print(overAllFriends[0][x])
        for x in range(len(overAllFriends[0])):
            k = []
            for j in range(len(ff)):
                if overAllFriends[0][x] == ff[j] and overAllFriends[0][x] != sk[0]['uid']:
                    k = ff[j]
                    findF.append(k)
        dataFriends["connection"].append(findF)
# print(dataFriends)

f = open("data_fileOK.json", "w", encoding = "utf-8")
json.dump(dataFriends, f, ensure_ascii=False)


print("test5")
