import requests

status = 'sold'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers = {'accept': 'application/json'})
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)
print(res.status_code)