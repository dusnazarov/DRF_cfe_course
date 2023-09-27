
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .mixins import StaffEditorPermissionMixin, BearTokenAuthenticationMixin



# #//////////////////////////////////////////////////////

class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.ListCreateAPIView):   
    
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.RetrieveAPIView):
    
     
    queryset = Product.objects.all()
    serializer_class = ProductSerializer        


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,
    generics.DestroyAPIView ):    
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.UpdateAPIView ):
        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    

