
from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from .mixins import StaffEditorPermissionMixin, BearTokenAuthenticationMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status


# ///////////////////////////////////////

class ProductMixinView (
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView ):
        
            
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'  
    
    def get(self, request, pk=None, *args, **kwargs):       
        pk = self.kwargs.get("pk")      
        
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 
            

# ///////////////////////////////////////
@api_view(['GET','POST','PUT', 'DELETE'])
def product_function_view(request, pk=None, *args, **kwargs):
        
    if request.method == "GET": 
        if pk is not None:
           obj = get_object_or_404(Product, pk=pk)
           serializer = ProductSerializer(obj, many=False)
           return Response(serializer.data)
             
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
        
    if request.method == 'POST':           
        serializer = ProductSerializer(data=request.data)        
        if serializer.is_valid(raise_exception=True):           
            serializer.save()            
            return Response(serializer.data)        
        return Response({"invalid":"not good data"}, status=400)
    
    if request.method == 'PUT':
        obj = get_object_or_404(Product, pk=pk)         
        serializer = ProductSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)

    if request.method == 'DELETE':
        obj = get_object_or_404(Product, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# #//////////////////////////////////////////////////////

class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.ListCreateAPIView,
    
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.RetrieveAPIView,
    ):
     
    queryset = Product.objects.all()
    serializer_class = ProductSerializer        


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,
    generics.DestroyAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.UpdateAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    

