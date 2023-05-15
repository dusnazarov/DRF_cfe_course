
#  ///////// ModelViewSet /////////
from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ 
    get -> list -> Question
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update ->
    patch -> Partial Update
    delete -> destroy 
    """    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

#  ///////// GenericViewSet /////////

# class ProductGenericViewSet(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     # mixins.CreateModelMixin,
#     # mixins.UpdateModelMixin,
#     # mixins.DestroyModelMixin,
#     viewsets.GenericViewSet):
    
#     """ 
#     get -> list -> Question
#     get -> retrieve -> Product Instance Detail View
#     post -> create -> New Instance
#     put -> Update ->
#     patch -> Partial Update
#     delete -> destroy 
#     """    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
    