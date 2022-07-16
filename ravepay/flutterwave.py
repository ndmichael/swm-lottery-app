from django.conf import settings
import requests


class Flutterwave:
    FLUTTERWAVE_SECRET_KEY = settings.FLUTTERWAVE_SECRET_KEY

    def verify_payment(self, ref, *args, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.FLUTTERWAVE_SECRET_KEY}",
            "Content-Type": "application/json",
        }
        url = " https://api.flutterwave.com/v3/payments"
        response = requests.post(url, headers=headers)
        print("response: ", response.json())

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data["data"]

        response_data = response.json()
        return response_data["status"], response_data["message"]
