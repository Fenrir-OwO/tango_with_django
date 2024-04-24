from django.urls import path

from . import views #import "views" from the current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view1"),
]