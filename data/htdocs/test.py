#!C:\Server\bin\Python\Python39\python.exe
# -*- coding: cp1251 -*-
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

print("test2")

form = cgi.FieldStorage() 
f = open("C:/login.txt", "r")
vk_session = vk_api.VkApi(f.readline(), f.readline())
vk_session.auth()
vk = vk_session.get_api()

name = form.getvalue("name")
surName = form.getvalue("surName")
bdate = form.getvalue("bdate")
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
if form.getvalue("city") !=None and country != None :
    city = vk.database.getCities(country_id = country, q= form.getvalue("city"))["items"][0]["id"]
else:
    city = None

searchResults=vk.users.search(q = name + ' ' + surName,  birth_day = bday, birth_month = bmonth,  birth_year = byear, sex = sex,  country = country, city = city, count = 100, fields='bdate, city, photo_200_orig, screen_name')

print("test3")
returnResults = []
print(int(searchResults['count']))

print("test8")
print(len(searchResults['items']))

for i in range(len(searchResults['items'])):
    print(i)
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
    # print(g)
    returnResults.append(g)
# print(returnResults[0][0])

f = open('res.txt', 'w', encoding = "utf-8")
for item in returnResults:
    f.write("%s;%s;%s;%s;%s;%s;%s\n" % (item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
f.close

print("test4")
print ("</body></html>")