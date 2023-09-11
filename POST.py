import requests

body = {"id": "0", "petId": "0", "quantity": "0", "shipDate": "2023-08-21T20:22:57.833Z", "status": "placed", "complete": "true"}
res = requests.post('https://petstore.swagger.io/v2/store/order', headers = {'accept': 'application/json'}, json = body)
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)
print(res.status_code)