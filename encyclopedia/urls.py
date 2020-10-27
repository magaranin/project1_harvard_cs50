from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry_page, name="entry_page"),
    path("create_new_entry", views.create_new_entry, name="create_new_entry"),
    path("search", views.search, name="search"),
    path("error_page", views.error_page, name="error_page")
]
