import requests
import json

identificador = 9
response = requests.post( "http://localhost:5000/push", params={'ID':identificador})
print(response.json())