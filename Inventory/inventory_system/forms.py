from crispy_forms.helper import FormHelper
from django import forms
from .models import *
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
User = get_user_model()


class laptop_form(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True

    class Meta:
        model = laptops
        fields = ('type', 'price', 'brand', 'status',
                  'issues', 'shipping')


class desktop_form(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True

    class Meta:
        model = desktops
        fields = ('type', 'price', 'brand', 'status',
                  'issues', 'shipping')


class smartphones_form(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True

    class Meta:
        model = smartphones
        fields = ('type', 'price', 'brand', 'status',
                  'issues', 'shipping')


class headphones_form(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True

    class Meta:
        model = headphones
        fields = ('type', 'price', 'brand', 'status',
                  'issues', 'shipping')


class consoles_form(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True

    class Meta:
        model = consoles
        fields = ('type', 'price', 'brand', 'status',
                  'issues', 'shipping')

# class userlogin_form(forms.Form):
#     helper = FormHelper()
#     helper.form_show_labels = True
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError('Check the credentials ')
#             if not user.check_password(password):
#                 raise forms.ValidationError('Check the password ')
#             if not user.is_active:
#                 raise forms.ValidationError('This is not a valid user')

#         return super(userlogin_form, self).clean(*args, **kwargs)


# class userregister_form(forms.ModelForm):

#     # the username is not required to be passed over here.. it is already passed in the meta.
#     email = forms.EmailField(label='Email Address')
#     email2 = forms.EmailField(label=' Confirm Email Address')
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'email2',
#             'password'
#         ]

#     def clean(self, *args, **kwargs):
#         email = self.cleaned_data.get('email')
#         email2 = self.cleaned_data.get('email2')
#         if email != email2:
#             raise forms.ValidationError('emails do not match')
#         email_qs = User.objects.filter(email=email)
#         if email_qs.exists():
#             raise forms.ValidationError('This email is already being used')
#         return super(userregister_form, self).clean(*args, **kwargs)
