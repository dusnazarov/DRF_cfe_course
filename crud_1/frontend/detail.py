import requests


product_id = input("Enter the product id \n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

endpoint = f"http://127.0.0.1:8000/products/{product_id}/detail/"

get_response = requests.get(endpoint)
print(get_response.json())


