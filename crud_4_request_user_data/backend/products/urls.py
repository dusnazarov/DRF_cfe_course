from django.urls import path
from .import views 


urlpatterns = [
    path('list/', views.ProductListCreateAPIView.as_view(), name="product-list"),    
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name="product-delete"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="product-edit"),
    path('<int:pk>/detail/', views.ProductDetailAPIView.as_view(), name="product-detail"),
]


