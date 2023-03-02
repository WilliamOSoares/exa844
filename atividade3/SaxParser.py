import xml.sax
import time

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.tipo = ""
    self.nome = ""
    self.lat = ""
    self.lon = ""
    self.dentroNode = False
    self.amenity = False
    self.name = False
    self.hasAmenity = False
    self.hasName = False

  def startElement(self, tag, attributes):   
    
    if tag =="node":  
      self.dentroNode = True
      self.lat = attributes.get("lat")
      self.lon = attributes.get("lon")
    if (tag =="tag" and self.dentroNode and attributes.get("k")=="amenity"):
      self.amenity = True
      self.hasAmenity = True
      self.tipo = attributes.get("v")
    if (tag =="tag" and self.dentroNode and attributes.get("k")=="name"):
      self.name = True
      self.hasName = True
      self.nome = attributes.get("v")

  def endElement(self, tag): 
    print(self.hasAmenity, self.hasName, self.amenity, self.name)
    if tag =="node" and self.hasAmenity and self.hasName:  
      self.dentroNode = False
      self.hasAmenity = False
      self.hasName = False
      print("lat:", self.lat) 
      print("lon:", self.lon)
    elif tag =="node" and not(self.hasAmenity) or not(self.hasName):
      self.dentroNode = False
      self.hasAmenity = False
      self.hasName = False
    if (tag =="tag" and self.dentroNode and self.amenity):
      self.amenity = False
      print("tipo:", self.tipo) 
    if (tag =="tag" and self.dentroNode and self.name):
      self.name = False
      print("nome:", self.nome)
      

inicio = time.time()
parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")
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