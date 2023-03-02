from pickle import FALSE, TRUE
from xml.dom.minidom import parse
import time

mapCentroFSA = parse('map.osm')

print("Starting DOM Parser...")
print(mapCentroFSA)
inicio = time.time()
est=1
for c in mapCentroFSA.getElementsByTagName("node"):	
	tags = c.getElementsByTagName("tag")
	flagAmenity=False
	for d in tags:		
		if(d.getAttribute("k")=="amenity"):
			print("Estabelecimento numero: ", est)
			print("Tipo:", d.getAttribute("v"))
			flagAmenity=True
		if(d.getAttribute("k")=="name" and flagAmenity):
			print("Nome:", d.getAttribute("v"))
	if(flagAmenity):
		print("lat: ", c.getAttribute("lat"))
		print("lon: ", c.getAttribute("lon"))
		est+=1		
print("Estabelecimentos encontrados: ", est)
fim = time.time()
print("Tempo: ", fim - inicio)