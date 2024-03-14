from django.urls import path

from . import views

app_name = "canary"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
]