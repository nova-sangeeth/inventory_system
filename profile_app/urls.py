from django.conf.urls import url
from .views import profile, register

urlpatterns = [
    url(r"^profile/$", profile, name="profile"),
    url(r"^register/$", register, name="register"),
]
