from rest_framework import serializers 
from django.contrib.auth import get_user_model

UserModel = get_user_model()
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        read_only_fields = ["id"]
        exclude= ["password"]