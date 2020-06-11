from django.shortcuts import render
from .forms import profile_form
from .models import user_profile

# Create your views here.
def profile(request):

    return render(request, "profile.html")


def profile_registration(request):
    return render(request, "register.html")
