from django.urls import path
from . import views
urlpatterns = [
    path("students/", views.index, name="index"),
]
