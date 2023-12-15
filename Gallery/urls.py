from django.contrib import admin
from django.urls import path, include
from .views import add_artpieceview, galleryindexview
urlpatterns = [
    path("", add_artpieceview, name="add_artpiece"),
    path("index", galleryindexview, name="gallery"),
]