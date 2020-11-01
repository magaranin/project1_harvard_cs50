from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry_page, name="entry_page"),
    path("create_new_entry", views.create_new_entry, name="create_new_entry"),
    path("search", views.search, name="search"),
    path("error_page", views.error_page, name="error_page"),
    path("wiki/<str:title>/edit_page", views.edit_page, name="edit_page"),
    path("save_edits/", views.save_edits, name="save_edits"),
    path("wiki/", views.random_page, name="random_page"),
    path("wiki/<str:title>/delete_page", views.delete_page, name="delete_page"),
]
