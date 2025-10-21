from rest_framework import serializers 
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "first_name", "last_name", "email", "is_staff", "is_active"]
        
class UserCreateSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(default=False)
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        min_length=8
    )
    
    class Meta:
        model = UserModel
        fields = ["is_staff","first_name","last_name","email","password"]
