from .models import Bronze, Silver, Gold, Platinum, Jackpot, Megawin


def timer(request):
    bronze_data = Bronze.objects.filter(status=True).first()
    silver_data = Silver.objects.filter(status=True).first()
    gold_data = Gold.objects.filter(status=True).first()
    platinum_data = Platinum.objects.filter(status=True).first()
    jackpot_data = Jackpot.objects.filter(status=True).first()
    mega_data = Megawin.objects.filter(status=True).first()

    context = {
        "b_data": bronze_data,
        "s_data": silver_data,
        "g_data": gold_data,
        "p_data": platinum_data,
        "j_data": jackpot_data,
        "mega_data": mega_data,
    }
    return context
