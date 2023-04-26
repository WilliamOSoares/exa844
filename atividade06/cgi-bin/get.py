#!/usr/bin/env python
#coding: utf8
import os
from datetime import datetime
import json
from urllib.parse import parse_qs
from pathlib import Path

with open(str(Path('db.json'))) as file:
    mensagens = json.load(file)

qs = os.environ["QUERY_STRING"]
list = parse_qs(qs, encoding="latin-1")

msg = dict()
msg['name'] = list["nome"][0]
msg['end'] = list["end"][0]
msg['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


mensagens["Mensagens"].append(msg)


print("Content-type: text/html charset=utf-8")
print()
print("<html><head><title>Seu Post</title></head><body>")
print("Autor: "+ msg['name'] + "<br>")
print("Mensagens: "+ msg['end'] + "<br>")
print("Data: "+ msg['time'] + "<br>")
print()
print("<H1 align=\"center\">Todas as mensagens</H1>")
print()
i = 1
for x in range(len(mensagens["Mensagens"])):
    print("Mensagem: " + str(i)+ "<br>")
    print("Autor: "+ mensagens["Mensagens"][x]['name'] + "<br>")
    print("Mensagens: "+ mensagens["Mensagens"][x]['end'] + "<br>")
    print("Data: "+ mensagens["Mensagens"][x]['time'] + "<br>")
    i+=1
print("</body></html>")

with open(str(Path('db.json')), 'w') as file:
    json.dump(mensagens, file)