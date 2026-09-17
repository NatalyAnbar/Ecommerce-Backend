from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = models.User
        fields = ['id','username','email','password','confirm_password']

    def validate_password(self,value):
        if len(value) < 8:
            raise serializers.ValidationError('The password must be longer than 8 characters.')
        return value

    def validate(self,attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('The passwords do not match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = models.User.objects.create_user(**validated_data)
        return user