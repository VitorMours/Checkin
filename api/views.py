from django.shortcuts import render
from rest_framework import views 
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import UserListSerializer

class UserListView(views.APIView):
    
    serializer_class = UserListSerializer
    
    def get(self) -> None:
        return Response(status = status.HTTP_200_OK)