from django.shortcuts import render
from rest_framework.viewsets import mixins,GenericViewSet
from . import models,Serializers

class RegisterUser(GenericViewSet,mixins.CreateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = Serializers.UserSerializer