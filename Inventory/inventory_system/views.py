from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_laptops(request):
    items = laptops.objects.all()
    context = {
        'items': items,
        'header': 'laptops'
    }
    return render(request, 'index.html', context)


def display_desktops(request):
    items = desktops.objects.all()
    context = {
        'items': items,
        'header': 'desktops'
    }
    return render(request, 'index.html', context)


def display_smartphones(request):
    items = smartphones.objects.all()
    context = {
        'items': items,
        'header': 'smartphones'
    }
    return render(request, 'index.html', context)


def display_headphones(request):
    items = headphones.objects.all()
    context = {
        'items': items,
        'header': 'headphones'
    }
    return render(request, 'index.html', context)


# def add_laptop(request):
#     if request.method == "POST":
#         form = laptop_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = laptop_form()
#         return render(request, 'add_new.html', {'form': form})


# def add_desktop(request):
#     if request.method == "POST":
#         form = desktop_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = desktop_form()
#         return render(request, 'add_new.html', {'form': form})


# def add_smartphones(request):
#     if request.method == "POST":
#         form = smartphones_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = smartphones_form()
#         return render(request, 'add_new.html', {'form': form})


# def add_headphones(request):
#     if request.method == "POST":
#         form = headphones_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = headphones_form()
#         return render(request, 'add_new.html', {'form': form})

# ADDING ITEMS TO THE INVENTORY USING  ADD_FORMS
def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_laptop(request):
    return add_device(request, laptop_form)


def add_desktop(request):
    return add_device(request, desktop_form)


def add_smartphones(request):
    return add_device(request, smartphones_form)


def add_headphones(request):
    return add_device(request, headphones_form)


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


def edit_laptop(request, pk):
    return edit_device(request, pk, laptops, laptop_form)


def edit_desktop(request, pk):
    return edit_device(request, pk, desktops, desktop_form)


def edit_smartphones(request, pk):
    return edit_device(request, pk, smartphones, smartphones_form)


def edit_headphones(request, pk):
    return edit_device(request, pk, headphones, headphones_form)

def delete_laptop(request, pk):
    laptops.objects.filter(id=pk).delete()
    items =laptops.objects.all()
    context = {
        'items': items
    }
    return render(request,'index.html', context)

def delete_desktop(request, pk):
    desktops.objects.filter(id=pk).delete()
    items =desktops.objects.all()
    context = {
        'items': items
    }
    return render(request,'index.html', context)


def delete_headphones(request, pk):
    headphones.objects.filter(id=pk).delete()
    items =headphones.objects.all()
    context = {
        'items': items
    }
    return render(request,'index.html', context)
    
def delete_smartphones(request, pk):
    smartphones.objects.filter(id=pk).delete()
    items =smartphones.objects.all()
    context = {
        'items': items
    }
    return render(request,'index.html', context)