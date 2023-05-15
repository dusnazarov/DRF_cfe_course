
# #  ////////////////    DRF Generics RetrieveAPIView and  DRF Generics ListCreateAPIView    ///////////////////////
import requests

endpoint = "http://127.0.0.1:8000/api/products/create/"

data = {
    "title":"This field is dones"
       
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())



