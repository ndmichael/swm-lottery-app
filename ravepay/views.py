from django.shortcuts import render, get_object_or_404, redirect
from .forms import PaymentForm
from django.conf import settings
from django.contrib.auth.admin import User
from .models import Payment
from lottery.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def initiate_payment(request):
    if request.method == "POST":
        p_form = PaymentForm(request.POST)
        if p_form.is_valid():
            payment = p_form.save(commit=False)
            payment.user = request.user
            payment.save()
            context = {
                "payment": payment,
                "flutterwave_public_key": settings.FLUTTERWAVE_PUBLIC_KEY,
            }
            return render(request, "ravepay/make_payment.html", context)
    else:
        p_form = PaymentForm()
    return render(request, "ravepay/initiate_payment.html", {"p_form": p_form})


@login_required
def verify_payment(request, ref):
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        user = Profile.objects.get(user=request.user)
        user.balance += payment.amount
        user.save()
        messages.success(request, "Payment Verification successful")
    else:
        messages.error(request, "Payment Verification failed.")
    return redirect("initiate-payment")
