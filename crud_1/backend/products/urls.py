from django.urls import path
from .import views 


# ///////////////////////////////////////////////

urlpatterns = [

    # ////// CRUD Class Based View ( generics ) ////////
    path('list/', views.ProductListCreateAPIView.as_view(), name="product-list"),     
    path('create/', views.ProductListCreateAPIView.as_view(), name="product-create"),     
    path('delete/<int:pk>/', views.ProductDestroyAPIView.as_view(), name="product-delete"),
    path('update/<int:pk>/', views.ProductUpdateAPIView.as_view(), name="product-edit"),
    path('detail/<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-detail"),

    # //////   CRUD Class Based View (mixins and generics)
    path('mlist/', views.ProductCRUDMixinView.as_view(), name="mproduct-list"),
    path('mcreate/', views.ProductCRUDMixinView.as_view(), name="mproduct-create" ),  
    path('mdetail/<int:pk>/', views.ProductCRUDMixinView.as_view(), name="mproduct-detail"), 
    path('mdelete/<int:pk>/', views.ProductCRUDMixinView.as_view(), name="mproduct-delete"), 
    path('mupdate/<int:pk>/', views.ProductCRUDMixinView.as_view(), name="mproduct-edit"),
    

    # ////// CRUD  Function Based View   ////////
    path('flist/', views.product_CRUD_function_view, name="fproduct-list"),
    path('fcreate/', views.product_CRUD_function_view, name="fproduct-create"),    
    path('fdetail/<int:pk>/', views.product_CRUD_function_view, name="fproduct-detail"),
    path('fupdate/<int:pk>/', views.product_CRUD_function_view, name="fproduct-edit"),
    path('fdelete/<int:pk>/', views.product_CRUD_function_view, name="fproduct-delete"),

    
]





