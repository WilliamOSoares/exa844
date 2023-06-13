from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

resultado = info_geral.find_one({'numero':'001'})
resultado2 = info_termos.find_one({'palavra':'teste'})

if resultado or resultado2:
    print(resultado)
    print(resultado2)
else:
    print("Opa, deu errado!")

# Criar indice para a busca ficar eficiente