from django import forms
from .models import *
from django import forms


class laptop_form(forms.ModelForm):
    class Meta:
        model = laptops
        fields = ("type", "price", "brand", "status", "issues", "shipping")


class desktop_form(forms.ModelForm):
    class Meta:
        model = desktops
        fields = ("type", "price", "brand", "status", "issues", "shipping")


class smartphones_form(forms.ModelForm):

    class Meta:
        model = smartphones
        fields = ("type", "price", "brand", "status", "issues", "shipping")


class headphones_form(forms.ModelForm):
    class Meta:
        model = headphones
        fields = ("type", "price", "brand", "status", "issues", "shipping")


class consoles_form(forms.ModelForm):
    class Meta:
        model = consoles
        fields = ("type", "price", "brand", "status", "issues", "shipping")
