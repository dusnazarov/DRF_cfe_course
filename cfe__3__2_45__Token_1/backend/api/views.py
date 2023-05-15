
from django.http import JsonResponse
import json

# 1)  ////////////////////////////////////////////////
# def api_home(request, *args, **kwargs):
#     return JsonResponse({"message":"Hi there, this is  your Django API response!!"})


# 2) ////////////////////////////////////////////////
# def api_home(request, *args, **kwargs):
#     # print(dir(request))    
#     # print(request.body)
#     # print(request.GET)  # url query params    
#     # return JsonResponse({"message":"Hi there, this is  your Django API response!!"})
    
#     body = request.body  # byte strings of JSON data
#     data = {}
        
#     try:
#         data = json.loads(body) # strings of JSON data -> Python Dict
#     except:
#         pass
#     print(data)
#     data['headers'] = dict(request.headers) 
#     data['content_type'] = request.content_type
#     data['params'] = dict(request.GET)    
#     return JsonResponse(data)

# 3) ///////////// Django Model Instance as an API Response ////////////////////////
# from django.http import JsonResponse
# from products.models import Product


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first() 
    
#     data = {}
#     if model_data:
#         data["id"] = model_data.id
#         data["title"] = model_data.title
#         data["content"] = model_data.content
#         data["price"] = model_data.price
   
#     return JsonResponse(data)

# 4) /////////////   Django Model Instance to Dictionary ////////////////////////
# from django.http import JsonResponse
# from products.models import Product
# from django.forms.models import model_to_dict


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first() 
    
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id','title'])        
   
#     return JsonResponse(data)

# 5) ///////////// Rest Framework View & Response  ////////////////////////
# from products.models import Product
# from django.forms.models import model_to_dict
# from rest_framework.response import Response
# from rest_framework.decorators import api_view 


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """ 
#     DRF API View
#     """
#     model_data = Product.objects.all().order_by("?").first() 
    
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id','title', 'price'])       
   
#     return Response(data)


# 6) ///////////// Django Rest Framework Model Serializer ////////////////////////
# from products.models import Product
# from django.forms.models import model_to_dict
# from rest_framework.response import Response
# from rest_framework.decorators import api_view 
# from products.serializers import ProductSerializer

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first() 
    
#     data = {}
#     if instance:        
#         data = ProductSerializer(instance).data 
   
#     return Response(data)


# 7) ///////////// Injest Data with Django Rest Framework Views  ////////////////////////
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)       
        return Response(serializer.data)
    return Response({"invalid":"not good data"}, status=400)


    



