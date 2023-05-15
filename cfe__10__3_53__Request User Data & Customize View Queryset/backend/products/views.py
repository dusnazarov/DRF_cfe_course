# # ///////////////////////   without Mixins   ///////////////////////
# # ///////////////////////   DRF Class Based View    ///////////////////////
# from rest_framework import generics
# from .models import Product
# from .serializers import ProductSerializer
# from api.mixins import StaffEditorPermissionMixin


# # //////////////// DRF Generics RetrieveAPIView   ///////////////////////
# class ProductDetailAPIView(
#     StaffEditorPermissionMixin,    
#     generics.RetrieveAPIView):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer    
   
# product_detail_view = ProductDetailAPIView.as_view()


# # //////////////// DRF Generics ListCreateAPIView   ///////////////////////
# class ProductListCreateAPIView(
#     StaffEditorPermissionMixin,
#     generics.ListCreateAPIView):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
     
    
#     def perform_create(self, serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')  or None
#         if content is None:
#             content = title
#         serializer.save(user=self.request.user, content=content)
    
#     def get_queryset(self, *args, **kwargs):
#         qs = super().get_queryset(*args, **kwargs)
#         request = self.request
#         user = request.user
#         if not user.is_authenticated:
#             return Product.objects.none()
#         print(request.user)
#         return qs.filter(user=request.user)
       
# product_list_create_view = ProductListCreateAPIView.as_view()


# # //////////////// DRF Generics UpdateAPIView   ///////////////////////
# class ProductUpdateAPIView(
#     StaffEditorPermissionMixin,
#     generics.UpdateAPIView):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

    
#     def perform_update(self, serializer):
#         instance = serializer.save()
       
#         if not instance.content:
#             instance.content = instance.title               
    
# product_update_view = ProductUpdateAPIView.as_view()

# # //////////////// DRF Generics DestroyAPIView   ///////////////////////
# class ProductDestroyAPIView(
#     StaffEditorPermissionMixin,
#     generics.DestroyAPIView):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
   
    
#     def perform_destroy(self, instance):
#        super().perform_destroy(instance)  
       
# product_delete_view = ProductDestroyAPIView.as_view()


# ///////////////////////  with Mixins  ///////////////////////

# ///////////////////////   DRF Class Based View    ///////////////////////
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin


# //////////////// DRF Generics RetrieveAPIView   ///////////////////////
class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,    
    generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
   
product_detail_view = ProductDetailAPIView.as_view()


# //////////////// DRF Generics ListCreateAPIView   ///////////////////////
class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
     
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')  or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        
       
product_list_create_view = ProductListCreateAPIView.as_view()


# //////////////// DRF Generics UpdateAPIView   ///////////////////////
class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    
    def perform_update(self, serializer):
        instance = serializer.save()
       
        if not instance.content:
            instance.content = instance.title               
    
product_update_view = ProductUpdateAPIView.as_view()

# //////////////// DRF Generics DestroyAPIView   ///////////////////////
class ProductDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
   
    
    def perform_destroy(self, instance):
       super().perform_destroy(instance)  
       
product_delete_view = ProductDestroyAPIView.as_view()






          
 

   

    

           

    


