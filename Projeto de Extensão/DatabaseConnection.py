from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import time
uri = "mongodb+srv://alunoEXA844:12345abc@cluster0.idqxuob.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.get_database('Doc_info')
info_geral = db.get_collection('documentos')
info_termos = db.get_collection('termos')

docTest = {
    'ID': '2016#002', #Será construido com ano#numero
    'numero': '003',
    'ano': '2016',
    'data': '13:06:2016',
    'reitor': 'Evandro',
    'cabecalho': 'Um teste',
    'texto': 'Isso é só um teste',
    'link': 'uefs.br',
    'cadastro': time.strftime('%d-%m-%Y'),
    'user': 'joao@uefs.br',
    'wd': '4.341' #Será calculado pela API
}

termoTest = {
    'palavra': 'Isso',
    'lista': [('2016#003',1)]
}

info_geral.insert_one(docTest)
info_termos.insert_one(termoTest)