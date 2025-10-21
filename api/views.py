from django.shortcuts import render
from rest_framework import views 
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import UserListSerializer, UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
class UserListView(views.APIView):
    
    serializer_class = UserCreateSerializer
    
    def get(self, format=None) -> Response:
        users = User.objects.all()    
        serialized_users = UserListSerializer(users, many=True)
        return Response(
            {   
             "message":"Users fetched successfully",
             "users":serialized_users.data
            },
            status=status.HTTP_200_OK
        )
    
    def post(self, request, format=None) -> Response:
        
        try:
            data = request.data.copy()
            password = data.get("password")

            if not password:
                return Response(
                    {"message": "Cannot continue with request because password is empty"}, 
                    status = status.HTTP_400_BAD_REQUEST
                )
                
            serialized_data = UserCreateSerializer(data=data, many=False)
            if serialized_data.is_valid():
                new_user = User(
                    first_name=serialized_data.validated_data["first_name"],
                    last_name=serialized_data.validated_data["last_name"],
                    email=serialized_data.validated_data["email"],
                    is_staff=serialized_data.validated_data["is_staff"],
                )
                new_user.set_password(serialized_data.validated_data["password"])
                new_user.save()                

                return Response({"message":"valid data in serializer"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {
                    "message":"An error occured in the request",
                    "error":str(e)
                },
                status = status.HTTP_400_BAD_REQUEST
            )