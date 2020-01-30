from django import forms
from .models import *


class laptop_form(forms.ModelForm):
    class Meta:
        model = laptops
        fields = ('type', 'price', 'brand', 'status', 'issues')


class desktop_form(forms.ModelForm):
    class Meta:
        model = desktops
        fields = ('type', 'price', 'brand', 'status', 'issues')


class smartphones_form(forms.ModelForm):
    class Meta:
        model = smartphones
        fields = ('type', 'price', 'brand', 'status', 'issues')


class headphones_form(forms.ModelForm):
    class Meta:
        model = headphones
        fields = ('type', 'price', 'brand', 'status', 'issues')
