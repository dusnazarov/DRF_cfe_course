import requests

endpoint = "http://127.0.0.1:8000/products/list/"

data = {
    "title":"This field is done now 8",
    "content":"my content",
    "price":129.00
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())