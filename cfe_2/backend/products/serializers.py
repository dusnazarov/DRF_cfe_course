from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse


# # 1)  ///////////////////////////////////////
# class ProductSerializer(serializers.ModelSerializer):   
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     url = serializers.SerializerMethodField(read_only=True)
    
#     class Meta:
#         model = Product
#         fields = ['url','pk','title','content','price', 'sale_price', 'my_discount' ]

#     def get_url(self, obj):
#         return f"/products/{obj.pk}/"
 
#     def get_my_discount(self, obj):
#         x = hasattr(obj, 'id')
#         print(x)
#         if not x:
#             return None
        
#         y = isinstance(obj, Product)
#         print(y)
#         if not y:
#             return None
             
#         return obj.get_discount()

# # 2)  ///////////////////////////////////////

class ProductSerializer(serializers.ModelSerializer):   
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    
    class Meta:
        model = Product
        fields = ['url', 'edit_url', 'pk','title', 'content','price', 'sale_price', 'my_discount' ]

    def get_url(self, obj):
        request = self.context.get('request') # self.request
        # print(self.context)
        # print(request)        

        if request is None:
            return None   
            
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request') # self.request

        if request is None:
            return None
               
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

     
    def get_my_discount(self, obj):
        x = hasattr(obj, 'id')     
        if not x:
            return None
        
        y = isinstance(obj, Product)     
        if not y:
            return None
             
        return obj.get_discount()

        
