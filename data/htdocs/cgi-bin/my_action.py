
#! /usr/bin/python3
# -*- coding: UTF-8 -*-
import cgi, sys
import vk_api # Импорт API

print("Content-type: text/html\n")

form = cgi.FieldStorage()  # получение данных из формы

html = """
<TItle>my_action.py</TItle>
<H1>Hello World!</H1>
<HR>
<H4>%s</H4>
<H4>%s</H4>
</HR>"""

f = open("C:\login.txt", "r")
vk_session = vk_api.VkApi(f.readline(), f.readline())
vk_session.auth()
vk = vk_session.get_api()

searchResults=vk.users.search(q = form['user_name'] + ' ' + form['user_surname'],  birth_day = int(form['user_bd.day']), birth_month = int(form['user_bd.month']),  birth_year = int(form['user_bd.year']), sex = form.getvalue('user_sex'),  age_from = int(form['user_ageFrom']), age_to = int(form['user_ageTo']),  country = form.getvalue('user_country_S'), city = vk.database.getCities(country_id = form.getvalue('user_country_S'), q= form['user_city']),  company = form['user_job_AS'], count = 100, fields='bdate, city, photo_50')
 
for i in searchResults["items"]:
    id = searchResults["items"][i]["id"]
    name = searchResults["items"][i]["first_name"] + " " + searchResults["items"][i]["last_name"]
    photo = searchResults["items"][i]["photo_50"]
    city = searchResults["items"][i]["city"]["title"]
    bday = searchResults["items"][i]["bdate"]
    print(id + "\n" + photo + "\n" + name + "\n" + city + "\n" + bday + "\n")

#print(html%(searchResults)) # вывод полученных данных
