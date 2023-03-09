import requests
from bs4 import BeautifulSoup

pages = ["https://exa-844-eight.vercel.app/",
"https://exa844-yotl.vercel.app/",
"https://antonio-raian.github.io/exa844/atividade1/",
"https://exa-844-a62ds125v-antonyaraujo.vercel.app/",
"https://exa-844-ten.vercel.app/Atividade1",
"https://exa-844-7teieiwsj-biancasantana1.vercel.app/Atividade_1",
"https://exa844-esdras.vercel.app/atividade1",
"https://exa844-seven.vercel.app/atividade1",
"https://exa-844-i32kyua3l-gabcarvas.vercel.app/",
"https://exa844-chi.vercel.app/",
"https://exa844-kevin.vercel.app/atividade1/index.html",
"https://laerciosr.github.io/exa844/atividade1/",
"https://falsomoralista.github.io/exa844/atividade1/",
"https://exa844-mariana.vercel.app/atividade1",
"https://exa-844-mu.vercel.app/",
"https://exa-844-orcin.vercel.app/Atividade1",
"https://ozenilsoncruz.github.io/exa844/atividade1/",
"https://silas-silva.github.io/EXA844/Atividade01/",
"https://exa844-virid.vercel.app/atividade1",
"https://programming-for-networks.vercel.app/activities/atividade1/",
"https://exa844-theta.vercel.app/",
"https://exa844-weslei-santos.vercel.app/",
"https://williamosoares.github.io/exa844/atividade1/index"]

outputFile = open("data.html", "w", encoding="utf8")
outputFile.write("<html> <head> <title>Atividade 5 - William</title> </head><body>")
for i in pages:
  print(i)
  page = requests.get(i)

  soup = BeautifulSoup(page.text, 'html.parser')

  #print("Título:", soup.title.string)
  outputFile.write("<p> Título: " + soup.title.string + "</p>")

  for img in soup.find_all('img'):
    #print("src: ", img.attrs.get("src"))
    outputFile.write('<img src="' + img.attrs.get("src") + '">')
    break

  