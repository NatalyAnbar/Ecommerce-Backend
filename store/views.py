from rest_framework.viewsets import ModelViewSet
from . import models,serializer


class CategoryView(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer
    lookup_field = 'slug'


class ProductView(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    lookup_field = 'slug'


class ProductImageView(ModelViewSet):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializer.ImageSerializer