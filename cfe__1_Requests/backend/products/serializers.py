
# 1)  ////////////////  Django Rest Framework Model Serializer    ///////////////////////
# from rest_framework import serializers
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Product
#         fields = ['id','title','content','price', 'sale_price','my_discount']
    
#     def get_my_discount(self, obj):
#         # print(obj)
#         # print(obj.id)
#         # print(obj.title)
#         # print(obj.price)
#         # print(obj.sale_price)              
#         # print(obj.get_discount)     
                
#         return obj.get_discount()  
    
# 2)  ////////////////  Injest Data with Django Rest Framework Views   ///////////////////////
# from rest_framework import serializers
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Product
#         fields = ['id','title','content','price', 'sale_price','my_discount']
        
#     def get_my_discount(self, obj):
#         try:        
#             return obj.get_discount()
#         except:
#             return None       
        
        
# 3)  ////////////////  DRF Class Based View and DRF Function Based View   ///////////////////////
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['title','content','price', 'sale_price','my_discount']
    
    # def get_my_discount(self, obj):
    #     print(obj.id)
    #     return obj.get_discount() 
    
    def get_my_discount(self, obj):
        try:        
            return obj.get_discount()
        except:
            return None       
    
    

       
    