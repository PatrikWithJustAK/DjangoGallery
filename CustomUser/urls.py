from django.contrib import admin
from django.urls import path, include
from .views import mainpageview, loginview, indexview, signupview 
urlpatterns = [
    path("", mainpageview, name="main"),
   path("login/", loginview, name = "login"),
   path("index/", indexview, name = "index"),
   path("signup/", signupview, name ="signup"),
]