import xml.sax
import time

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.tipo = ""
    self.nome = ""
    self.lat = ""
    self.lon = ""
    self.dentroNode = False
    self.hasAmenity = False
    self.hasNameAndAmenity = False
    self.est=1

  def startElement(self, tag, attributes):   
    
    if tag =="node":  
      self.dentroNode = True
      self.lat = attributes.get("lat")
      self.lon = attributes.get("lon")
      self.hasAmenity = False
      self.hasNameAndAmenity = False
    if (tag =="tag" and self.dentroNode and attributes.get("k")=="amenity"):
      self.hasAmenity = True
      self.tipo = attributes.get("v")
    if (tag =="tag" and self.dentroNode and attributes.get("k")=="name" and self.hasAmenity):
      self.hasNameAndAmenity = True
      self.nome = attributes.get("v")
      
  def endElement(self, tag): 
    
    if tag =="node" and self.hasAmenity and self.hasNameAndAmenity:  
      self.dentroNode = False
      self.hasAmenity = False
      self.hasNameAndAmenity = False
      print("Estabelecimento numero: ", self.est)
      print("tipo:", self.tipo) 
      print("nome:", self.nome)
      print("lat:", self.lat) 
      print("lon:", self.lon)
      self.est+=1
      

inicio = time.time()
parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("atividade3/map.osm")
print("Estabelecimentos encontrados: ", Handler.est)
fim = time.time()
print("Tempo: ", fim - inicio)

'''
import xml.sax
import time

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.clientId = ""

  def startElement(self, tag, attributes):    
    self.currentData = ""
    
    if tag =="Cliente":  
      self.clientId = attributes.get("id")  

  def endElement(self, tag):    
    if tag =="nome":	
      print("Nome:", self.currentData) 
      print("id:", self.clientId) 

  def characters(self, content):	
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("Banco.xml")
'''