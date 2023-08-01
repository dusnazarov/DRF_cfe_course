from django.urls import path
from .import views 

# //////////////////////////////////


# urlpatterns = [
#     path('list/', views.ProductMixinView.as_view(), name="product-list"),
#     path('create/', views.ProductMixinView.as_view(), name="product-create" ),  
#     path('<int:pk>/detail/', views.ProductMixinView.as_view(), name="product-detail"), 
#     path('<int:pk>/delete/', views.ProductMixinView.as_view(), name="product-delete"), 
#     path('<int:pk>/update/', views.ProductMixinView.as_view(), name="product-edit"), 
# ]

# ////////////////////////////////////////


# urlpatterns = [
#     path('list/', views.product_function_view, name="product-list"),
#     path('create/', views.product_function_view, name="product-create"),    
#     path('<int:pk>/detail/', views.product_function_view, name="product-detail"),
#     path('<int:pk>/update/', views.product_function_view, name="product-edit"),
#     path('<int:pk>/delete/', views.product_function_view, name="product-delete"),

# ]

# ///////////////////////////////////////////////

urlpatterns = [
    path('list/', views.ProductListCreateAPIView.as_view(), name="product-list"),    
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name="product-delete"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="product-edit"),
    path('<int:pk>/detail/', views.ProductDetailAPIView.as_view(), name="product-detail"),
]


