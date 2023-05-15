
#  ////////////////  DRF Generics ListAPIView  and DRF Generics ListCreateAPIView   ///////////////////////
import requests

endpoint = "http://127.0.0.1:8000/api/products/list/"
data = {
    "title":"This field is dones"
}

get_response = requests.get(endpoint, json=data)
print(get_response.json())







