import requests
import json
import time
url = "https://sa-east-1.aws.data.mongodb-api.com/app/data-nfnyx/endpoint/data/v1/action/findOne"
payload_term = json.dumps({
    "collection": "termos",
    "database": "Doc_info",
    "dataSource": "Cluster0",
    "projection": {
        'palavra': 'Um',
        'lista': [('2016#002',2)]
    }
})

payload_doc = json.dumps({
    "collection": "documentos",
    "database": "Doc_info",
    "dataSource": "Cluster0",
    "projection": {
        'ID': '2016#002', #Será construido com ano#numero
        'numero': '001',
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
})

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'sfEUS5IaWA6U8SEzgu5N2CHD8XhdDTixvsiA57T9EeKVRjUtg893G2kqbbS7Ij43',
}

response1 = requests.request("POST", url, headers=headers, data=payload_doc)
response2 = requests.request("POST", url, headers=headers, data=payload_term)

print(response1.text)
print(response2.text)