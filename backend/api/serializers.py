from rest_framework import serializers

from .models import Journey
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt import serializers as jwtserializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password", "is_active", "is_staff")
        extra_kwargs = {
            "password": {"write_only": True},
            "is_active": {"read_only": True},
            "is_staff": {"read_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

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
        full_name = f"{getattr(self.user, 'first_name', '')} {getattr(self.user, 'last_name', '')}".strip()
        data["name"] = full_name or self.user.email
        data["email"] = self.user.email
        data["id"] = str(self.user.id)
        return data


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = "__all__"


