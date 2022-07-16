from django.urls import path
from .views import initiate_payment, verify_payment


urlpatterns = [
    path("make_payment/", initiate_payment, name="initiate-payment"),
    path("<str:ref>/", verify_payment, name="verify-payment"),
]
