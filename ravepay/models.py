from django.db import models
from django.contrib.auth.admin import User
import secrets
from .flutterwave import Flutterwave

# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self) -> str:
        return f"payment: {self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            objects_with_similar_ref = Payment.objects.filter(ref=ref)
            if not objects_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount

    def verify_payment(self):
        flutterpay = Flutterwave()
        status, result = flutterpay.verify_payment(self.ref, self.amount)
        # self.verified = True
        if status:
            self.verified = True
            self.save()
        if self.verified:
            return True
        return False
