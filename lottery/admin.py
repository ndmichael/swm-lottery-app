from django.contrib import admin
from .models import (
    Profile,
    Drawing,
    Ticket,
    Pick,
    WinningPick,
    Bronze,
    Silver,
    Gold,
    Platinum,
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Drawing)

admin.site.register(Bronze)
admin.site.register(Silver)
admin.site.register(Gold)
admin.site.register(Platinum)

admin.site.register(Ticket)
admin.site.register(Pick)
admin.site.register(WinningPick)
