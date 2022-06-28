from django.urls import path
from adminapp.views import index, admin_games

urlpatterns = [
    path("staff/type/<str:game_type>/", admin_games, name="admin_games"),
    path("staff/<str:username>/", index, name="admin_index"),
]
