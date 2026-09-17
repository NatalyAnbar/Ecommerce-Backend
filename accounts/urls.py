from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

rouetr = DefaultRouter()
rouetr.register('register',views.RegisterUser)

urlpatterns = [
    path('',include(rouetr.urls))
]