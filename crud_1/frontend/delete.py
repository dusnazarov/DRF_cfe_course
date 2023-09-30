import requests

product_id = input("Enter the product id \n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

if product_id:
    endpoint = f"http://127.0.0.1:8000/products/delete/{product_id}/"

    # /////////// ModelViewSet //////////////
    endpoint = f"http://127.0.0.1:8000/viewsets/products/{product_id}"
    
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)