import requests

product_id = input("Enter the product id \n")

headers = {
    "Authorization": f"Bearer ee01f86010799a069bcdc49955d6e093dbfb3ba2"
}



endpoint = f"http://127.0.0.1:8000/products/{product_id}/update/"

data = {
    "title":"Hello world my old friend 1",
    "content":"my content",
    "price":129.00
}

get_response = requests.put(endpoint, json=data, headers=headers)
print(get_response.json())
