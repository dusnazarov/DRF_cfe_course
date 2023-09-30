import requests

product_id = input("Enter the product id \n")

endpoint = f"http://127.0.0.1:8000/products/update/{product_id}/"

# /////////// ModelViewSet //////////////
endpoint = f"http://127.0.0.1:8000/viewsets/products/{product_id}/"


data = {
    "title":"Hello world my old friend 2",
    "content":"my content 2",
    "price":130.00
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
