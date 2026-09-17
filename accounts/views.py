from django.shortcuts import render
from rest_framework.viewsets import mixins,GenericViewSet
from . import models,serializer

class RegisterUser(GenericViewSet,mixins.CreateModelMixin):
    queryset = models.User.objects.all()
    model = models.User
    serializer_class = serializer.UserSerializer