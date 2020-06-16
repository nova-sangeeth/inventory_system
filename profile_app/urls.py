from django.conf.urls import url
from .views import profile, register, edit_profile

urlpatterns = [
    url(r"^profile/$", profile, name="profile"),
    url(r"^register/$", register, name="register"),
    url(r"^edit_profile/$", edit_profile, name="edit_profile"),
]
