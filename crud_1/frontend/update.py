import requests

product_id = input("Enter the product id \n")

endpoint = f"http://127.0.0.1:8000/products/{product_id}/update/"

data = {
    "title":"Hello world my old friend 1",
    "content":"my content",
    "price":129.00
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
