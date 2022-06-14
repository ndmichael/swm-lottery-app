from django.urls import path
from .views import index, games


urlpatterns = [
    path('', index, name="index"),
    path('games/', games, name="all-games")
]