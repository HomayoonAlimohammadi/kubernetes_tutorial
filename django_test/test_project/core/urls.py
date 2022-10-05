from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path("users/", views.user_list, name="user_list"),
    path("users/<int:pk>", views.user_details, name="user_details"),
    path("users/create", views.user_create, name="user_create"),
]
