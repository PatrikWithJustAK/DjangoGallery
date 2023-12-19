from django.contrib import admin
from django.urls import path, include
from .views import add_artpieceview, galleryindexview, deleteartpiece_view
urlpatterns = [
    path("", add_artpieceview, name="add_artpiece"),
    path("dashboard/", galleryindexview, name="dashboard"),
    path("deleteart/<int:pk>", deleteartpiece_view, name ="delete_artpiece"),
]