
#  ////////////////  DRF Generics ListAPIView  and DRF Generics ListCreateAPIView   ///////////////////////
# import requests

# endpoint = "http://127.0.0.1:8000/api/products/list/"
# data = {
#     "title":"This field is dones"
# }

# get_response = requests.get(endpoint, json=data)
# print(get_response.json())


#  //////////////// Create Token   ///////////////////////
# import requests
# from getpass import getpass

# auth_endpoint = "http://127.0.0.1:8000/api/auth/"
# password = getpass()


# auth_response = requests.post(auth_endpoint, json={"username":"admin", "password":password })
# print(auth_response.json())

#  //////////////// Authorization  ///////////////////////
# import requests
# from getpass import getpass

# auth_endpoint = "http://127.0.0.1:8000/api/auth/"

# username = input("What is your username?\n")
# password = getpass("What is your password?\n")

# auth_response = requests.post(auth_endpoint, json={"username":username, "password":password })
# print(auth_response.json())

# if auth_response.status_code == 200:
#     token = auth_response.json()['token']
  
#     headers = {
#         "Authorization": f"Token {token}"
#     }
#     endpoint = "http://127.0.0.1:8000/api/products/list/"
#     get_response = requests.get(endpoint, headers=headers)
    
#     print(get_response.json())
    

#  //////////////// Authorization with Bearer ///////////////////////
import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"

username = input("What is your username?\n")
password = getpass("What is your password?\n")

auth_response = requests.post(auth_endpoint, json={"username":username, "password":password })
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
  
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/list/"
    get_response = requests.get(endpoint, headers=headers)
    
    print(get_response.json())
    
    
    









