from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User, Group 
from backend.api.infra.web.serializers import UserSerializer

class UserView(APIView):
    """
    View for the user object inside of the api
    """
    def get(self, request) -> None:
        """
        Return a list with the classes in the database
        """
        users = User.objects.all()
        serialized_data = UserSerializer(users, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request) -> None:
        """
        Create a new element inside of the group
        """
        serialized_data = UserSerializer(data=request.data)
        print(serialized_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request) -> None:

        pass 


    def delete(self, request):
        pass

    
