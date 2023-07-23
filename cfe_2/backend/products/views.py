
from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from .mixins import StaffEditorPermissionMixin, BearTokenAuthenticationMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status


# ////////////////   DRF Mixin and Generic API View   ///////////////////////

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
        # print(self.args, self.kwargs)
        
        pk = self.kwargs.get("pk")
        # print(pk)
        
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 
            

# //////////////// DRF Function Based View ///////////////////////

@api_view(['GET','POST','PUT', 'DELETE'])
def product_function_view(request, pk=None, *args, **kwargs):
        
    if request.method == "GET": 
        if pk is not None:
           obj = get_object_or_404(Product, pk=pk)
           serializer = ProductSerializer(obj, many=False, context={'request':request})
           return Response(serializer.data)
             
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)
        
    if request.method == 'POST':           
        serializer = ProductSerializer(data=request.data, context={'request':request})        
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')  or None
            if content is None:
                content = title
            serializer.save(content=content)            
            return Response(serializer.data)        
        return Response({"invalid":"not good data"}, status=400)
    
    if request.method == 'PUT':
        obj = get_object_or_404(Product, pk=pk)         
        serializer = ProductSerializer(obj, data=request.data, context={'request':request})
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

       
    def perform_create(self, serializer):
              
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')  or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailAPIView(    
    generics.RetrieveAPIView,
    ):
     
    queryset = Product.objects.all()
    serializer_class = ProductSerializer        


class ProductDestroyAPIView(
    generics.DestroyAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        print(instance)
        super().perform_destroy(instance)      


class ProductUpdateAPIView(    
    generics.UpdateAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    
    def perform_update(self, serializer):
        instance = serializer.save()
       
        if not instance.content:
            instance.content = instance.title                   
    





