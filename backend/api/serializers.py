from rest_framework import serializers
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt import serializers as jwtserializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'

# class ManagerSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Manager
        # fields = '__all__'

class CustomJWTSerializer(jwtserializers.TokenObtainPairSerializer):
    username_field = 'email'

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["id"] = str(user.id)
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data["name"] = self.user.name
        data["email"] = self.user.email
        data["id"] = self.user.id
        return data