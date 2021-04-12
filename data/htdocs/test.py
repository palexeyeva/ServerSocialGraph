#!C:\Users\1371851\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: UTF-8 -*-
print ("Content-type: text/html\n\n")
print
print ("<html><head>")
print ("")
print ("</head><body>")
print ("Hello.")

import cgi  
# import vk_api 

print("test2")

form = cgi.FieldStorage() 


f = open("C:/login.txt", "r")


print("test3")
print(form)

def index():
    postData = form
    json = str(postData['param'].value)
    print(json)


print ("</body></html>")
