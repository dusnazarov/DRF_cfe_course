
# #  1) //////////////// ///////////////////////
# from rest_framework import serializers
# from .models import Product
# from rest_framework.reverse import reverse
# from . import validators
# from api.serializers import UserPublicSerializer


# class ProductSerializer(serializers.ModelSerializer):
#     # user = UserPublicSerializer(read_only=True)
#     owner = UserPublicSerializer(source='user', read_only=True)
    
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     edit_url = serializers.SerializerMethodField(read_only=True)
#     url = serializers.HyperlinkedIdentityField(
#         view_name='product-detail',
#         lookup_field='pk'
#         )
#     title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    
#     class Meta:
#         model = Product
#         fields = [
#             'owner',
#             'id',            
#             'edit_url',
#             'url',            
#             'title',
#             'content',
#             'price', 
#             'sale_price',
#             'my_discount'
#         ]
         
        
#     def get_edit_url(self, obj):     
#         request = self.context.get('request')    
                   
#         if request is None:
#             return None
#         return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)
    
    
#     def get_my_discount(self, obj):
#         try:        
#             return obj.get_discount()
#         except:
#             return None


# 2)  //////////////// ///////////////////////
# from rest_framework import serializers
# from .models import Product
# from rest_framework.reverse import reverse
# from . import validators
# from api.serializers import UserPublicSerializer


# class ProductSerializer(serializers.ModelSerializer):    
#     owner = UserPublicSerializer(source='user', read_only=True)    
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     edit_url = serializers.SerializerMethodField(read_only=True)
#     url = serializers.HyperlinkedIdentityField(
#         view_name='product-detail',
#         lookup_field='pk'
#         )
#     title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    
#     class Meta:
#         model = Product
#         fields = [
#             'owner',
#             'id',            
#             'edit_url',
#             'url',            
#             'title',
#             'content',
#             'price', 
#             'sale_price',
#             'my_discount'
#         ]
         
        
#     def get_edit_url(self, obj):     
#         request = self.context.get('request')    
                   
#         if request is None:
#             return None
#         return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)
    
    
#     def get_my_discount(self, obj):
#         try:        
#             return obj.get_discount()
#         except:
#             return None


# 3)  //////////////// ///////////////////////
from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from . import validators
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
        )
    title = serializers.CharField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):    
    owner = UserPublicSerializer(source='user', read_only=True)
    related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
       
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
        )
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    
    class Meta:
        model = Product
        fields = [
            'owner',
            'pk',            
            'edit_url',
            'url',            
            'title',
            'content',
            'price', 
            'sale_price',
            'my_discount',
            'related_products'
        ]
         
        
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
        
        

        
    
    
         

    
    

       
    