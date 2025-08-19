from django.shortcuts import render 
from django.urls import path
from backend.api.infra.web import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path("users/", views.UserView.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)
