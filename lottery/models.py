from django.db import models
from django.contrib.auth.admin import User
from django.utils import timezone
import datetime
import secrets

# Create your models here.


class Profile(models.Model):
    gender = (("male", "MALE"), ("female", "FEMALE"), ("others", "OTHERS"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    city = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender, null=True, blank=True)
    dob = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}"


class Drawing(models.Model):
    choices = (
        ("bronze", "BRONZE"),
        ("silver", "SILVER"),
        ("gold", "GOLD"),
        ("platinum", "PLATINUM"),
    )
    type = models.CharField(max_length=20, choices=choices)
    created = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    def enddate(self):
        return self.created + datetime.timedelta(hours=1)

    def __str__(self):
        return f"{self.type}"


class Ticket(models.Model):
    drawing_id = models.OneToOneField(
        Drawing, on_delete=models.CASCADE, related_name="draw_ticket"
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ticket"
    )
    status = models.BooleanField(default=False)
    ticket_id = models.CharField(max_length=50, default="")
    correct_count = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        while not self.ref:
            ticket_id = secrets.token_urlsafe(8)
            objects_with_similar_ticket_id = Ticket.objects.filter(ticket_id=ticket_id)
            if not objects_with_similar_ticket_id:
                self.ticket_id = ticket_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"


class Pick(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_pick"
    )
    ticket_id = models.OneToOneField(
        Ticket, on_delete=models.CASCADE, related_name="ticket_pick"
    )
    ball_number = models.CharField(max_length=6)
    special_number = models.CharField(max_length=1)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.ball_number}{self.special_number}"


class WinningPick(models.Model):
    drawing_id = models.OneToOneField(
        Drawing, on_delete=models.CASCADE, related_name="winning_draw"
    )
    correct_number = models.CharField(max_length=7)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id}"
