from django.urls import path
from clients.views import update_profile


urlpatterns = [
    path(r"profile/<str:username>/settings/", update_profile, name="update_profile"),
]
