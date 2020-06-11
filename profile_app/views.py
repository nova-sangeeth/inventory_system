from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import profile_form
from .models import user_profile
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    return render(request, "profile.html")


def profile_registration(request):
    return render(request, "register.html")
