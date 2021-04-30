#!C:\Server\bin\Python\Python39\python.exe
# -*- coding: cp1251 -*-

import vk_api 


def captcha_handler(captcha):

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)
 
f = open("C:/login.txt", "r")
vk_session = vk_api.VkApi(f.readline(), f.readline(), captcha_handler=captcha_handler)
vk_session.auth()
