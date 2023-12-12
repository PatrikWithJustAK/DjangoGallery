from django.contrib import admin
from django.urls import path, include
from .views import Mainpageview
urlpatterns = [
    path("", Mainpageview.as_view()),
]