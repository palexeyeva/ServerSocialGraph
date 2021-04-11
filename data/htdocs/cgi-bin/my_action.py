
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

vk_session = vk_api.VkApi('+79172991547', 'GHBITVlbgkjv{EQcjc`v130521')
vk_session.auth()
vk = vk_session.get_api()

'''regularSearch=vk.users.search(q = form['user_name'] + ' ' + form['user_surname'],
 birth_day = form['user_bd.day'], birth_month = form['user_bd.month'], 
 birth_year = form['user_bd.year'], sex = form['user_sex'], 
 age_from = form['user_ageFrom'], age_to = form['user_ageTo'], country = form['user_country'], city = form['user_city'], count = 100, fields='bdate, city')

print(html%(regularSearch)) # вывод полученных данных'''

advancedSearch=vk.users.search(q = form['user_name'] + ' ' + form['user_surname'],
 birth_day = int(form['user_bd.day']), birth_month = int(form['user_bd.month']), 
 birth_year = int(form['user_bd.year']), sex = form['user_sex'].value, 
 age_from = int(form['user_ageFrom']), age_to = int(form['user_ageTo']), country = form['user_country_S'], city = vk.database.getCities(country_id = form['user_country_S'], q= form['user_city']), 
 company = form['user_job_AS'], count = 100, fields='bdate, city, photo_50')

print(html%(advancedSearch)) # вывод полученных данных
