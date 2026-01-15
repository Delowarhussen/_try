from django.urls import path

from books import views

urlpatterns = [
    path("ok/",views.ok),
]
