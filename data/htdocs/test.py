#!C:\Users\1371851\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: cp1251 -*-
print ("Content-type: text/html\n\n")
print
print ("<html><head>")
print ("")
print ("</head><body>")
print ("Hello.")

import cgi  
import json

# import vk_api 

print("test2")

form = cgi.FieldStorage() 


# f = open("C:/login.txt", "r")


print("test3")
print(form.getvalue("name"))


 
print("test4")
print ("</body></html>")
