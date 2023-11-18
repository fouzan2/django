from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("about/", views.about_fun, name="about"),
    path("contactus/", views.contactus_fun, name="contact"),
    path("login/", views.login_fun, name="login"),
]
 