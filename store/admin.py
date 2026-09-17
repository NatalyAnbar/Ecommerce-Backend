from django.contrib import admin
from . import models

admin.site.site_header = 'Admin Panel'

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug':['name']}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','brand','price']
    list_filter = ['name','brand']
    search_fields = ['name','brand']
    prepopulated_fields = {'slug' : ['name']}


@admin.register(models.ProductImage)
class ImageAdmin(admin.ModelAdmin):
    fields = ['title']   


