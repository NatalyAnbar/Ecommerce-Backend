from rest_framework import serializers
from . import models

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['id','product','img','title','is_main']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    uploaded_img = serializers.ListField(
            child = serializers.ImageField(
                allow_empty_file=False),
                write_only = True)
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = models.Product
        fields = ['id','category','slug','name','brand','description','price','uploaded_img','images']

    def create(self, validated_data):
        images = validated_data.pop('uploaded_img')
        product = models.Product.objects.create(**validated_data)
        for img in images:
            models.ProductImage.objects.create(product=product,img=img)
        return product
    

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    products = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = models.Category
        fields = ['id','name','slug','products']





