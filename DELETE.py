import requests

petid = '9223372036854769000'

res = requests.delete(f'https://petstore.swagger.io/v2/pet/{petid}', headers = {'accept': 'application/json'})
print(res.text)
print(res.status_code)