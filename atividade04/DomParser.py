from pickle import FALSE, TRUE
from xml.dom.minidom import parse
import time
import json

geoJson = dict()
geoJson['type'] = "FeatureCollection"
geoJson['features'] = []

mapCentroFSA = parse('map.osm')

print("Starting DOM Parser...")
print(mapCentroFSA)
inicio = time.time()
est=1
for c in mapCentroFSA.getElementsByTagName("node"):	
	coordinates = []
	geometry = dict()
	properties = dict()
	features = dict()
	tags = c.getElementsByTagName("tag")
	flagAmenity=False
	flagNome=False
	for d in tags:		
		if(d.getAttribute("k")=="amenity"):
			print("Estabelecimento numero: ", est)
			amenityTipo = d.getAttribute("v")
			flagAmenity=True
		if(d.getAttribute("k")=="name" and flagAmenity):
			nome = d.getAttribute("v")
			flagNome=True
	if(flagAmenity and flagNome):
		properties['nome'] = nome #print("Nome:", d.getAttribute("v"))
		properties['tipo'] = amenityTipo #print("Tipo:", amenityTipo)
		coordinates.append(float(c.getAttribute("lon"))) #print("lon: ", c.getAttribute("lon"))
		coordinates.append(float(c.getAttribute("lat"))) #print("lat: ", c.getAttribute("lat"))
		geometry['type'] = "Point"
		geometry['coordinates'] = coordinates
		features['type'] = "Feature"
		features['geometry'] = geometry
		features['properties'] = properties
		geoJson['features'].append(features)
		est+=1		
print("Estabelecimentos encontrados: ", est)
jsonStr = json.dumps(geoJson, indent=4, ensure_ascii=False)
print(jsonStr)
jsonStrTxt = json.loads(jsonStr)
with open("atividade4.json", "w") as outfile:
	json.dump(jsonStrTxt, outfile)
fim = time.time()
print("Tempo: ", fim - inicio)