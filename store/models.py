from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='products')
    slug = models.SlugField()
    name = models.CharField(max_length=100, db_index=True)
    brand = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(validators=[MinValueValidator(0)], max_digits=5, decimal_places=2, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='',blank=True)
    title = models.CharField(max_length=100, blank=True)
    is_main = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return self.title