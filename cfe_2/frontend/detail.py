import requests

endpoint = "http://127.0.0.1:8000/products/1/detail/"

get_response = requests.get(endpoint)
print(get_response.json())


