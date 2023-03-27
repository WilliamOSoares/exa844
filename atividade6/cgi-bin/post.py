#!/usr/bin/env python
#coding: utf8
import os, cgi
import time
import json

form = cgi.FieldStorage()

inputFile = open("http://localhost:8000/cgi-bin/db.json", "r")

with open("http://localhost:8000/cgi-bin/db.json") as file:
    mensagens = json.load(file)

msg = dict()
msg['name'] = form["nome"].value
msg['end'] = form["end"].value
msg['time'] = time.time()


mensagens["mensagens"].append(msg)


print("Content-type: text/html; charset=utf-8")
print()
print("<html><head><title>Seu Post</title></head><body>")
print("Autor: "+ msg['name'] + "<br>")
print("Mensagens: "+ msg['end'] + "<br>")
print("Data: "+ msg['time'] + "<br>")
print()
print("<H1 align=\"center\">Todas as mensagens</H1>")
print()
i = 1
for x in range(len(mensagens["mensagens"])):
    print("Mensagem: " + str(i))
    print("Autor: "+ x['name'] + "<br>")
    print("Mensagens: "+ x['end'] + "<br>")
    print("Data: "+ x['time'] + "<br>")
    i+=1
print("</body></html>")

with open("http://localhost:8000/cgi-bin/db.json", 'w') as file:
    json.dump(mensagens, file)