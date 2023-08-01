
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .mixins import StaffEditorPermissionMixin, BearTokenAuthenticationMixin, UserQuerySetMixin
          


# # # 1) ///////////////////////////////////
# class ProductListCreateAPIView(    
#     BearTokenAuthenticationMixin,
#     StaffEditorPermissionMixin,    
#     generics.ListCreateAPIView,
    
#     ):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None

#         if content is None:
#             content = title
#         serializer.save(user=self.request.user, content=content)

#     # def get_queryset(self, *args, **kwargs): 
#     #     print(kwargs)    
#     #     # print(self.request.user)
#     #     qs = super().get_queryset(*args, **kwargs)
#     #     # print(qs)
#     #     return  qs 
            

#     def get_queryset(self, *args, **kwargs):
#         qs = super().get_queryset(*args, **kwargs)
#         # print(qs)        
#         user = self.request.user        
#         # print(user.is_authenticated)
#         # print(user)
#         if not user.is_authenticated:
#             return Product.objects.none()        
#         return qs.filter(user=self.request.user)         
             
        

# class ProductDetailAPIView(
#     StaffEditorPermissionMixin,
#     BearTokenAuthenticationMixin,    
#     generics.RetrieveAPIView,
#     ):
     
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer        


# class ProductDestroyAPIView(
#     StaffEditorPermissionMixin,
#     BearTokenAuthenticationMixin,
#     generics.DestroyAPIView
#     ):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'


# class ProductUpdateAPIView(
#     StaffEditorPermissionMixin,
#     BearTokenAuthenticationMixin,    
#     generics.UpdateAPIView
#     ):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk' 


# # 2) ///////////////////////////////////
class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.ListCreateAPIView,
    
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

        

class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.RetrieveAPIView,
    ):
     
    queryset = Product.objects.all()
    serializer_class = ProductSerializer        


class ProductDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,
    generics.DestroyAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    BearTokenAuthenticationMixin,    
    generics.UpdateAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    
    