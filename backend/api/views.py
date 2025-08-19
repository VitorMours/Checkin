from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

class UserView(APIView):
    """
    
    """
    def get(self, request) -> None:
        """
        Return a list with the classes in the database
        """
        pass

    def post(self, request) -> None:
        """
        Create a new element inside of the group
        """
        pass