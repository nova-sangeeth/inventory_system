from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')


# def login_view(request):
#     next = request.GET.get('next')
#     form = userlogin_form(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('/')
#     context = {
#         'form': form,
#     }
#     return render(request, "login.html", context)


# def registeration_view(request):
#     next = request.GET.get('next')
#     form = userregister_form(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         # save the credentials from the form to the 'user' object.
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username=user.username, password=password)
#         login(request, new_user)
#         if next:
#             return redirect(next)
#         return redirect('/')
#     context = {
#         'form': form,
#     }
#     return render(request, "registeration.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

# DISPLAY FUNCTIONALIITIES
@login_required
def display_laptops(request):
    items = laptops.objects.all()
    context = {
        'items': items,
        'header': 'laptops'
    }
    return render(request, 'index.html', context)


@login_required
def display_desktops(request):
    items = desktops.objects.all()
    context = {
        'items': items,
        'header': 'desktops'
    }
    return render(request, 'index.html', context)


@login_required
def display_smartphones(request):
    items = smartphones.objects.all()
    context = {
        'items': items,
        'header': 'smartphones'
    }
    return render(request, 'index.html', context)


@login_required
def display_headphones(request):
    items = headphones.objects.all()
    context = {
        'items': items,
        'header': 'headphones'
    }
    return render(request, 'index.html', context)


@login_required
def display_consoles(request):
    items = consoles.objects.all()
    context = {
        'items': items,
        'header': 'consoles'
    }
    return render(request, 'index.html', context)

# ADD FUNTIONALITIES
@login_required
def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


@login_required
def add_laptop(request):
    return add_device(request, laptop_form, )


@login_required
def add_desktop(request):
    return add_device(request, desktop_form, )


@login_required
def add_smartphones(request):
    return add_device(request, smartphones_form, )


@login_required
def add_headphones(request):
    return add_device(request, headphones_form, )


@login_required
def add_consoles(request):
    return add_device(request, consoles_form, )

# EDIT FUNCTIONALITIES
@login_required
def edit_device(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})


@login_required
def edit_laptop(request, pk):
    return edit_device(request, pk, laptops, laptop_form)


@login_required
def edit_desktop(request, pk):
    return edit_device(request, pk, desktops, desktop_form)


@login_required
def edit_smartphones(request, pk):
    return edit_device(request, pk, smartphones, smartphones_form)


@login_required
def edit_headphones(request, pk):
    return edit_device(request, pk, headphones, headphones_form)


@login_required
def edit_consoles(request, pk):
    return edit_device(request, pk, consoles, consoles_form)

# THE DELETE FUNCTIONALITIES
@login_required
def delete_laptop(request, pk):
    laptops.objects.filter(id=pk).delete()
    items = laptops.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


@login_required
def delete_desktop(request, pk):
    desktops.objects.filter(id=pk).delete()
    items = desktops.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


@login_required
def delete_headphones(request, pk):
    headphones.objects.filter(id=pk).delete()
    items = headphones.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


@login_required
def delete_smartphones(request, pk):
    smartphones.objects.filter(id=pk).delete()
    items = smartphones.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


@login_required
def delete_consoles(request, pk):
    consoles.objects.filter(id=pk).delete()
    items = consoles.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)
