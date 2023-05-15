  
# 1)  //////////////// ///////////////////////
# from rest_framework import serializers
# from .models import Product
# from rest_framework.reverse import reverse

# class ProductSerializer(serializers.ModelSerializer):
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     url = serializers.SerializerMethodField(read_only=True)  
    
#     class Meta:
#         model = Product
#         fields = ['id', 'url', 'title','content','price', 'sale_price','my_discount']
        
    
#     def get_url(self, obj):     
#         request = self.context.get('request') 
                   
#         if request is None:
#             return None
#         return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)
    
    
#     def get_my_discount(self, obj):
#         try:        
#             return obj.get_discount()
#         except:
#             return None
        
   
# 2)  //////////////// ///////////////////////
from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
        )
    
    class Meta:
        model = Product
        fields = ['id', 'edit_url', 'url', 'title','content','price', 'sale_price','my_discount']
    
        
    def get_edit_url(self, obj):     
        request = self.context.get('request')    
                   
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)
    
    
    def get_my_discount(self, obj):
        try:        
            return obj.get_discount()
        except:
            return None
         

    
    

       
    