from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^display_laptops$", display_laptops, name="display_laptops"),
    url(r"^display_desktops$", display_desktops, name="display_desktops"),
    url(r"^display_smartphones$", display_smartphones, name="display_smartphones"),
    url(r"^display_headphones$", display_headphones, name="display_headphones"),
    url(r"^display_consoles$", display_consoles, name="display_consoles"),
    # adding info to the database links
    url(r"^add_laptop$", add_laptop, name="add_laptop"),
    url(r"^add_desktop$", add_desktop, name="add_desktop"),
    url(r"^add_smartphones$", add_smartphones, name="add_smartphones"),
    url(r"^add_headphones$", add_headphones, name="add_headphones"),
    url(r"^add_consoles$", add_consoles, name="add_consoles"),
    # editing the info in the database:
    url(r"^edit_laptop/(?P<pk>\d+)$", edit_laptop, name="edit_laptop"),
    url(r"^edit_desktop/(?P<pk>\d+)$", edit_desktop, name="edit_desktop"),
    url(r"^edit_smartphones/(?P<pk>\d+)$", edit_smartphones, name="edit_smartphones"),
    url(r"^edit_consoles/(?P<pk>\d+)$", edit_consoles, name="edit_consoles"),
    url(r"^edit_headphones/(?P<pk>\d+)$", edit_headphones, name="edit_headphones"),
    # DELETE VIEWS URLS
    url(r"^delete_laptop/(?P<pk>\d+)$", delete_laptop, name="delete_laptop"),
    url(r"^delete_desktop/(?P<pk>\d+)$", delete_desktop, name="delete_desktop"),
    url(
        r"^delete_smartphones/(?P<pk>\d+)$",
        delete_smartphones,
        name="delete_smartphones",
    ),
    url(
        r"^delete_headphones/(?P<pk>\d+)$", delete_headphones, name="delete_headphones"
    ),
    url(r"^delete_consoles/(?P<pk>\d+)$", delete_consoles, name="delete_consoles"),

]
