from django.conf.urls import url
from .views import profile, profile_registration

urlpatterns = [
    url(r"^profile$", profile, name="profile"),
    url(r"^profile_registration$", profile_registration, name="profile_registration"),
]
