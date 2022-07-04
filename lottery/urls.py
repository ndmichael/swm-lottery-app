from django.urls import path
from .views import index, games, draw, contact, about, faq, bonus, result, terms


urlpatterns = [
    path("", index, name="index"),
    path("games/", games, name="all-games"),
    path("games/draws/<str:type>/<int:id>/", draw, name="pick"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("faq/", faq, name="faq"),
    path("bonus/", bonus, name="bonus"),
    path("result/", result, name="result"),
    path("terms/", terms, name="terms"),
    path("drawing/", reset_draw, name="reset_draw"),
]
