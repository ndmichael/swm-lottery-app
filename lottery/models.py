from django.db import models
from django.contrib.auth.admin import User
from django.utils import timezone
import datetime
import secrets

# Create your models here.


class Profile(models.Model):
    states = (
        ("Abia State", "Abia State"),
        ("Adamawa State", "Adamawa State"),
        ("Akwa Ibom State", "Akwa Ibom State"),
        ("Anambra State", "Anambra State"),
        ("Bauchi State", "Bauchi State"),
        ("Bayelsa State", "Bayelsa State"),
        ("Benue State", "Benue State"),
        ("Borno State", "Borno State"),
        ("Cross River State", "Cross River State"),
        ("Delta State", "Delta State"),
        ("Ebonyi State", "Ebonyi State"),
        ("Edo State", "Edo State"),
        ("Ekiti State", "Ekiti State"),
        ("Enugu State", "Enugu State"),
        ("Gombe State", "Gombe State"),
        ("Imo State", "Imo State"),
        ("Jigawa State", "Jigawa State"),
        ("Kaduna State", "Kaduna State"),
        ("Kano State", "Kano State"),
        ("Katsina State", "Katsina State"),
        ("Kebbi State", "Kebbi State"),
        ("Kogi State", "Kogi State"),
        ("Kwara State", "Kwara State"),
        ("Lagos State", "Lagos State"),
        ("Nasarawa State", "Nasarawa State"),
        ("Niger State", "Niger State"),
        ("Ogun State", "Ogun State"),
        ("Ondo State", "Ondo State"),
        ("Osun State", "Osun State"),
        ("Oyo State", "Oyo State"),
        ("Plateau State", "Plateau State"),
        ("Rivers State", "Rivers State"),
        ("Sokoto State", "Sokoto State"),
        ("Taraba State", "Taraba State"),
        ("Yobe State", "Yobe State"),
        ("Zamfara State", "Zamfara State"),
    )
    gender = (("male", "MALE"), ("female", "FEMALE"), ("others", "OTHERS"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    city = models.CharField(max_length=30, null=True, blank=True, choices=states)
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
    created = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)

    def enddate(self):
        if self.type == "bronze":
            return self.created + datetime.timedelta(hours=0, minutes=2)
        elif self.type == "silver":
            return self.created + datetime.timedelta(hours=0, minutes=4)
        elif self.type == "gold":
            return self.created + datetime.timedelta(hours=0, minutes=6)
        elif self.type == "platinum":
            return self.created + datetime.timedelta(hours=0, minutes=8)
        else:
            return self.created

    def __str__(self):
        return f"{self.type}"


class Ticket(models.Model):
    drawing_id = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name="draw_ticket"
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ticket"
    )
    status = models.BooleanField(default=False)
    ticket_code = models.CharField(max_length=50, default="")
    correct_count = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        while not self.ticket_code:
            ticket_code = secrets.token_urlsafe(8)
            objects_with_similar_ticket_code = Ticket.objects.filter(
                ticket_code=ticket_code
            )
            if not objects_with_similar_ticket_code:
                self.ticket_code = ticket_code
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
    ball_number = models.CharField(max_length=50)
    special_number = models.CharField(max_length=20)
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
