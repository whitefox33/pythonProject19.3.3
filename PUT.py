import requests

body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.put('https://petstore.swagger.io/v2/pet', json=body)
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)
print(res.status_code)