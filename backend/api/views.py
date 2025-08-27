from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class UserView(APIView):

    def get(self) -> None:
        pass
    
    def post(self) -> None:
        pass
    
    def put(self) -> None:
        pass

    def delete(self) -> None:
        pass


class AdminView(APIView):

    def get(self) -> None:
        pass
    
    def post(self) -> None:
        pass
    
    def put(self) -> None:
        pass

    def delete(self) -> None:
        pass
