from django.shortcuts import render 
from django.urls import path

from checkin.infra.api import views


urlpatterns = [
    path("users/", views.UserView.as_view())
]
