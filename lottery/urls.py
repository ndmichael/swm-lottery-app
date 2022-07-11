from django.urls import path
from .views import (
    index,
    games,
    draw,
    contact,
    about,
    faq,
    bonus,
    result,
    terms,
    reset_bronze,
    reset_silver,
    reset_gold,
    reset_platinum,
    result_details,
)


urlpatterns = [
    path("", index, name="index"),
    path("games/", games, name="all-games"),
    path("games/draws/<str:type>/<int:id>/", draw, name="pick"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("faq/", faq, name="faq"),
    path("bonus/", bonus, name="bonus"),
    path("result/", result, name="result"),
    path("result/<str:type>/", result_details, name="result-details"),
    path("terms/", terms, name="terms"),
    path("drawing/reset_bronze", reset_bronze, name="reset_bronze"),
    path("drawing/reset_silver", reset_silver, name="reset_silver"),
    path("drawing/reset_gold", reset_gold, name="reset_gold"),
    path("drawing/reset_platinum", reset_platinum, name="reset_platinum"),
]
