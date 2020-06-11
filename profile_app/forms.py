from django import forms
from .models import user_profile


class profile_form(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = "__all__"
        exclude = ("user",)
