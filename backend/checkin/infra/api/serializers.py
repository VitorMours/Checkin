from rest_framework import serializers 
from checkin.infra.db.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ["id", "first_name", "last_name", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
