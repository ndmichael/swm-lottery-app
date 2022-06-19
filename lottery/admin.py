from django.contrib import admin
from .models import Profile, Drawing, Ticket, Pick, WinningPick

# Register your models here.
admin.site.register(Profile)
admin.site.register(Drawing)
admin.site.register(Ticket)
admin.site.register(Pick)