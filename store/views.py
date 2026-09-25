from rest_framework.viewsets import ModelViewSet
from . import models,Serializers


class CategoryView(ModelViewSet):

    # Fetch all categories
    queryset = models.Category.objects.all()
    serializer_class = Serializers.CategorySerializer
    lookup_field = 'slug'


class ProductView(ModelViewSet):

    # Fetch all products
    queryset = models.Product.objects.all()
    serializer_class = Serializers.ProductSerializer
    lookup_field = 'slug'


class ProductImageView(ModelViewSet):

    # view and manage product gallery images
    queryset = models.ProductImage.objects.all()
    serializer_class = Serializers.ImageSerializer