from rest_framework import serializers
from .models import Product



## //////////////////////////////////////

# class ProductSerializer(serializers.Serializer):  
#     title = serializers.CharField(max_length=120)
#     content = serializers.CharField(max_length=120)
#     price = serializers.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    
   
#     def create(self, validated_data):  
#         return Product.objects.create(**validated_data) 
     

#     def update(self, instance, validated_data):
#         print(validated_data)
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()        
#         return instance


## //////////////////////////////////////

class ProductSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Product
        fields = ['id','title', 'content', 'price']

    
     
        
