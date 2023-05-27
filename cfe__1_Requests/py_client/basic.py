
import requests

# 0) ///////////////////////////////////////// 
# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/"

# get_response = requests.get(endpoint)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON

# print(get_response.text)
# print(get_response.json())

# 0') /////////////////////////////////////////
# endpoint = "http://httpbin.org/anything"

# # get_response = requests.get(endpoint)

# """  
#     {
#         'data': '', 
#         'form': {},        
#         'json': None,
#     }
# """
 
# # get_response = requests.get(endpoint, json={"query":"Hello world"} )
# """ 
#     {
#         'data': '{"query": "Hello world"}',
#         'form': {},  
#         'Content-Type': 'application/json', 
#         'json': {'query': 'Hello world'}
#      }
# """

# get_response = requests.get(endpoint, data={"query":"Hello world"} )
# """ 
#     {
#         'data': '', 
#         'form': {'query': 'Hello world'},   
#         'Content-Type': 'application/x-www-form-urlencoded', 
#         'json': None
#     }
# """

# print(get_response.json())

# 1) ///////////////////////////////////////// 
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint)


# print(get_response.json())
# print(get_response.json()["message"])
# print(get_response.status_code)


# 2) ////////////////////////////////////////////// 
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint, params={"abc":123}, json={"message":"Hello world!!"})
# print(get_response.json())


# 2 ') ////////////////////////////////////////////// 
# endpoint = "http://127.0.0.1:8000/api/"

# # get_response = requests.get(endpoint, params={"abc":123}, json={"message":"Hello world!!"})
# get_response = requests.get(endpoint, params={"abc":123})
# print(get_response.json())


# 2 ' ') ////////////////////////////////////////////// 
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint, params={"abc":123}, json={"message":"Hello world!!"})
# print(get_response.json())

# 3)  ////////////  Django Model Instance as an API Response   //////////
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint)
# print(get_response.json())


# 4)  /////////////////   Django Model Instance to Dictionary //////////////
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint)
# print(get_response.json())


# 5) ///////////// Rest Framework View & Response  ////////////////////////
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint)
# print(get_response.json())

# 6)  /////////// Django Rest Framework Model Serializer ///////////////////////
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint)
# print(get_response.json())

# 7)  /////////// Injest Data with Django Rest Framework Views ///////////////////////

# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint, json={"title":"hello World!!!"})
# print(get_response.json())


# 7 ')  /////////// Injest Data with Django Rest Framework Views ///////////////////////
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.post(endpoint, json={"title":"hello World!!!"})
# print(get_response.json())

# 7 ' ')  /////////// Injest Data with Django Rest Framework Views ///////////////////////
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.post(endpoint, json={"product_id":"12"})
# print(get_response.json())

# 8)  /////////// Injest Data with Django Rest Framework Views ///////////////////////
# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.post(endpoint, json={"title":"Hello world"})
# print(get_response.json())











