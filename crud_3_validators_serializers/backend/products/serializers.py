from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from . import validators


# # # 1)  //////////////// Inline Validators ///////////////////////

# class ProductSerializer(serializers.ModelSerializer):   
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     edit_url = serializers.SerializerMethodField(read_only=True)
#     detail_url = serializers.HyperlinkedIdentityField(
#         view_name='product-detail',
#         lookup_field='pk'
#     )
    
#     class Meta:
#         model = Product
#         fields = ['detail_url', 'edit_url', 'pk', 'title', 'content','price', 'sale_price', 'my_discount' ]


#     def validate_title(self, value):
#         # qs = Product.objects.filter(title__exact=value)
#         qs = Product.objects.filter(title__iexact=value)
    
#         if qs.exists():
#         # print(qs.exists())
                    
#             raise serializers.ValidationError(f"{value} is already a product name")
#         return value
        

#     def get_url(self, obj):
#         request = self.context.get('request')            

#         if request is None:
#             return None   
            
#         return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

#     def get_edit_url(self, obj):
#         request = self.context.get('request') # self.request

#         if request is None:
#             return None
               
#         return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

     
#     def get_my_discount(self, obj):
          
#         if not hasattr(obj, 'id'):
#             return None
        
            
#         if not isinstance(obj, Product):
#             return None
             
#         return obj.get_discount()
        
# # 2)  ////////////////  External Validators ///////////////////////

# class ProductSerializer(serializers.ModelSerializer):   
#     my_discount = serializers.SerializerMethodField(read_only=True)   
#     edit_url = serializers.SerializerMethodField(read_only=True)
#     detail_url = serializers.HyperlinkedIdentityField(
#         view_name='product-detail',
#         lookup_field='pk'
#     )
    

#     # title = serializers.CharField(validators=[validators.validate_title])
#     title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    
#     class Meta:
#         model = Product
#         fields = ['detail_url', 'edit_url', 'pk', 'title', 'content','price', 'sale_price', 'my_discount' ]


#     def get_url(self, obj):
#         request = self.context.get('request')            

#         if request is None:
#             return None   
            
#         return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

#     def get_edit_url(self, obj):
#         request = self.context.get('request') 

#         if request is None:
#             return None
               
#         return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

     
#     def get_my_discount(self, obj):
             
#         if not hasattr(obj, 'id'):
#             return None        
           
#         if not isinstance(obj, Product):
#             return None
             
#         return obj.get_discount()

    
# # 3)  ///////////////////////////////////////

class ProductSerializer(serializers.ModelSerializer):   
    my_discount = serializers.SerializerMethodField(read_only=True)   
    edit_url = serializers.SerializerMethodField(read_only=True)
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    
    
    # title = serializers.CharField(validators=[validators.validate_title])
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    email = serializers.EmailField(write_only=True)

   
    
    class Meta:
        model = Product
        fields = ['detail_url', 'edit_url', 'pk', 'title', 'content','price', 'sale_price', 'my_discount', 'email']

    def create(self, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        print(validated_data)
        obj = super().create(validated_data)
        print(obj, email)
        return obj
        
        
        
    def update(self, instance, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        print(validated_data)        
        obj = super().update(instance, validated_data)
        print(obj, email)        
        return obj
    

    def get_url(self, obj):
        request = self.context.get('request')            

        if request is None:
            return None   
            
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request') 

        if request is None:
            return None
               
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

     
    def get_my_discount(self, obj):
             
        if not hasattr(obj, 'id'):
            return None        
           
        if not isinstance(obj, Product):
            return None
             
        return obj.get_discount()      
