from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import profile_form
from .models import user_profile
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    user = user_profile.objects.filter(user=request.user)
    return render(request, "profile.html", {"data": user})


def register(request):
    user = User.objects.get(username=request.user.username)
    user_profile_id = user_profile(user=user)
    form = profile_form(request.POST or None, instance=user_profile_id)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "register.html", {"form": form})
