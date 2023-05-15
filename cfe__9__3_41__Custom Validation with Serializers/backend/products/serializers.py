
# 1)  //////////////// Inline Validators ///////////////////////
# from rest_framework import serializers
# from .models import Product
# from rest_framework.reverse import reverse

# class ProductSerializer(serializers.ModelSerializer):
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     edit_url = serializers.SerializerMethodField(read_only=True)
#     url = serializers.HyperlinkedIdentityField(
#         view_name='product-detail',
#         lookup_field='pk'
#         )
    
    
#     class Meta:
#         model = Product
#         fields = ['id', 'edit_url', 'url', 'title','content','price', 'sale_price','my_discount']
    
   
#     def validate_title(self, value):
#         # qs = Product.objects.filter(title__exact=value)
#         qs = Product.objects.filter(title__iexact=value)
        
#         if qs.exists():
#             raise serializers.ValidationError(f"{value} is already a product name")
#         return value
   
     
        
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
        
# 2)  ////////////////  External Validators ///////////////////////
# from rest_framework import serializers
# from .models import Product
# from rest_framework.reverse import reverse
# from .validators import validate_title


# class ProductSerializer(serializers.ModelSerializer):
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     edit_url = serializers.SerializerMethodField(read_only=True)
#     url = serializers.HyperlinkedIdentityField(
#         view_name='product-detail',
#         lookup_field='pk'
#         )
#     title = serializers.CharField(validators=[validate_title])
    
#     class Meta:
#         model = Product
#         fields = ['id', 'edit_url', 'url', 'title','content','price', 'sale_price','my_discount']
    
   
#     def validate_title(self, value):
#         # qs = Product.objects.filter(title__exact=value)
#         qs = Product.objects.filter(title__iexact=value)
        
#         if qs.exists():
#             raise serializers.ValidationError(f"{value} is already a product name")
#         return value
   
     
        
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
        

# 3)  ////////////////  External Validators ///////////////////////
from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from . import validators


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
        )
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    
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
        
    
    
         

    
    

       
    