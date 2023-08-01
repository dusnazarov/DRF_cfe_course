from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):   
    my_discount = serializers.SerializerMethodField(read_only=True)

    
    class Meta:
        model = Product
        fields = ['pk','title','content','price', 'sale_price', 'my_discount' ]

        
    def get_my_discount(self, obj):
        x = hasattr(obj, 'id')
        # print(x)
        if not x:
            return None
        
        y = isinstance(obj, Product)
        # print(y)
        if not y:
            return None
             
        return obj.get_discount()

