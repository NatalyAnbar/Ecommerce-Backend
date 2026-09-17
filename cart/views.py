from rest_framework.viewsets import ModelViewSet
from . import models,serializer

class CartView(ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializer.CartSerializer
