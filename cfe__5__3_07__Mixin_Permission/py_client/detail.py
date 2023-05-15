
# ////////////////  DRF Generics RetrieveAPIView    ///////////////////////
# import requests

# endpoint = "http://127.0.0.1:8000/api/products/6/"

# get_response = requests.get(endpoint)
# print(get_response.json())

# ////////////////  DRF Generics RetrieveAPIView , Token Authorization    ///////////////////////
import requests
headers = {'Authorization':'Bearer e7ad55837b8c5bab074d7b2ecbbe550ce556ad94'}
endpoint = "http://127.0.0.1:8000/api/products/6/"

get_response = requests.get(endpoint, headers=headers)
print(get_response.json())












