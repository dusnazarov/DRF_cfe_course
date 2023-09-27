from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from . import validators



class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only=True, source='user')  
    edit_url = serializers.SerializerMethodField(read_only=True)
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'    )


    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
  
    
    class Meta:
        model = Product
        fields = ['owner','detail_url', 'edit_url', 'pk', 'title', 'content','price', 'sale_price']

   
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

     
  

    
        
