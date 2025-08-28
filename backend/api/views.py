from django.shortcuts import render

from .serializers import CustomJWTSerializer, UserSerializer
from .models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

# class ManagerViewSet(viewsets.ModelViewSet):

    # queryset = Manager.objects.all()
    # serializer_class = ManagerSerializer


class CustomJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

