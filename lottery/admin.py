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
    Jackpot,
    Megawin,
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Drawing)

admin.site.register(Bronze)
admin.site.register(Silver)
admin.site.register(Gold)
admin.site.register(Platinum)
admin.site.register(Jackpot)
admin.site.register(Megawin)

admin.site.register(Ticket)
admin.site.register(Pick)
admin.site.register(WinningPick)
