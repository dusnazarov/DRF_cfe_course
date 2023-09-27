import requests

product_id = input("Enter the product id \n")

headers = {
    "Authorization": f"Bearer ee01f86010799a069bcdc49955d6e093dbfb3ba2"
}


try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

if product_id:
    endpoint = f"http://127.0.0.1:8000/products/{product_id}/delete/"
    
    get_response = requests.delete(endpoint, headers=headers)
    print(get_response.status_code, get_response.status_code==204)