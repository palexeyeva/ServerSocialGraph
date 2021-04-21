#!C:\Users\1371851\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: cp1251 -*-
print ("Content-type: text/html\n\n")
print
print ("<html><head>")
print ("")
print ("</head><body>")
print ("Hello.")
import cgi  
import vk_api 
form = cgi.FieldStorage() 

val_id = int(form.getvalue("chooseID"))
print(val_id)

f = open("C:/login.txt", "r")
vk_session = vk_api.VkApi(f.readline(), f.readline())
print("test1")
vk_session.auth()
vk = vk_session.get_api()
print("test2")

getPersFriends = vk.friends.get(user_id = val_id, order='hints', count = 200, fields = 'nickname')
print("test3")

print(getPersFriends['items'][0]['first_name'].encode('utf-8').decode('cp1251'))


f = open('resSearch.txt', 'w', encoding = "utf-8")
for i in range(int(getPersFriends['count'])):
    f.write("%s " % getPersFriends['items'][i]['first_name'])
    f.write("%s\n" % getPersFriends['items'][i]['last_name'])
f.close


print ("</body></html>")