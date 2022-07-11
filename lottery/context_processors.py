from .models import Bronze, Silver, Gold, Platinum


def timer(request):
    bronze_data = Bronze.objects.filter(status=True).first()
    silver_data = Silver.objects.filter(status=True).first()
    gold_data = Gold.objects.filter(status=True).first()
    platinum_data = Platinum.objects.filter(status=True).first()

    context = {
        "b_data": bronze_data,
        "s_data": silver_data,
        "g_data": gold_data,
        "p_data": platinum_data,
    }
    return context
