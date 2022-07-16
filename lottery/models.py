from django.db import models
from django.contrib.auth.admin import User
from django.utils import timezone
from datetime import datetime, timedelta
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
        ("jackpot", "JACKPOT"),
        ("megawin", "MEGAWIN"),
    )
    type = models.CharField(max_length=20, choices=choices)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.type}-{self.id}"


class Bronze(models.Model):
    draw = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name="bronze_draw"
    )
    status = models.BooleanField(default=False)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.now)
    winning_set = models.BooleanField(default=False)

    class Meta:
        ordering = ("-startdate",)

    def save(self, *args, **kwargs):
        self.enddate = self.startdate + timedelta(minutes=5)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.draw} {self.startdate}"


class Silver(models.Model):
    draw = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name="silver_draw"
    )
    status = models.BooleanField(default=False)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.now)
    winning_set = models.BooleanField(default=False)

    class Meta:
        ordering = ("-startdate",)

    def save(self, *args, **kwargs):
        self.enddate = self.startdate + timedelta(days=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.draw} {self.startdate}"


class Gold(models.Model):
    draw = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name="gold_draw"
    )
    status = models.BooleanField(default=False)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default="")
    winning_set = models.BooleanField(default=False)

    class Meta:
        ordering = ("-startdate",)

    def save(self, *args, **kwargs):
        self.enddate = self.startdate + timedelta(days=3)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.draw} {self.startdate}"


class Platinum(models.Model):
    draw = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name="platinum_draw"
    )
    status = models.BooleanField(default=False)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.now)
    winning_set = models.BooleanField(default=False)

    class Meta:
        ordering = ("-startdate",)

    def save(self, *args, **kwargs):
        self.enddate = self.startdate + timedelta(days=7)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.draw} {self.startdate}"


class Jackpot(models.Model):
    draw = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name="jackpot_draw"
    )
    status = models.BooleanField(default=False)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.now)
    winning_set = models.BooleanField(default=False)

    class Meta:
        ordering = ("-startdate",)

    def save(self, *args, **kwargs):
        self.enddate = self.startdate + timedelta(minutes=7)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.draw} {self.startdate}"


class Megawin(models.Model):
    draw = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name="mega_draw"
    )
    status = models.BooleanField(default=False)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.now)
    winning_set = models.BooleanField(default=False)

    class Meta:
        ordering = ("-startdate",)

    def save(self, *args, **kwargs):
        self.enddate = self.startdate + timedelta(minutes=5)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.draw} {self.startdate}"


class BallNumbers(models.Model):
    ball = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ball}"


class Ticket(models.Model):
    bronze = models.ForeignKey(
        Bronze,
        on_delete=models.CASCADE,
        related_name="bronze_ticket",
        null=True,
        blank=True,
    )
    silver = models.ForeignKey(
        Silver,
        on_delete=models.CASCADE,
        related_name="silver_ticket",
        null=True,
        blank=True,
    )
    gold = models.ForeignKey(
        Gold,
        on_delete=models.CASCADE,
        related_name="gold_ticket",
        null=True,
        blank=True,
    )
    platinum = models.ForeignKey(
        Platinum,
        on_delete=models.CASCADE,
        related_name="platinum_ticket",
        null=True,
        blank=True,
    )
    jackpot = models.ForeignKey(
        Jackpot,
        on_delete=models.CASCADE,
        related_name="jackpot_ticket",
        null=True,
        blank=True,
    )
    megawin = models.ForeignKey(
        Megawin,
        on_delete=models.CASCADE,
        related_name="megawin_ticket",
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ticket"
    )
    status = models.BooleanField(default=False)
    draw_type = models.CharField(max_length=50, default="bronze")
    ticket_code = models.CharField(max_length=50, default="")
    correct_count = models.BooleanField(default=False)
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


class WinningPick(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="winning_ticket",
        null=True,
        blank=True,
    )
    correct_number = models.ManyToManyField(BallNumbers)
    special_number = models.CharField(max_length=10, default="")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id}"


class Pick(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_pick"
    )
    ticket_id = models.OneToOneField(
        Ticket,
        on_delete=models.CASCADE,
        related_name="ticket_pick",
    )
    ball_numbers = models.ManyToManyField(BallNumbers)
    special_number = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.ball_numbers}{self.special_number}"
