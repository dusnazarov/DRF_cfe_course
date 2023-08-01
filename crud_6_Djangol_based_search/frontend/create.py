import requests

headers = {
    "Authorization": f"Bearer ee01f86010799a069bcdc49955d6e093dbfb3ba2"
}

data = {
    "title":"This field is done  ",
    "content":"my book",
    "price":"23.23" 
       
}
    
endpoint = "http://127.0.0.1:8000/products/list/"
    
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())