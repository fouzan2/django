from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.welcome, name="welcome"),
    path("about/", views.about_fun, name="about"),
    path("contactus/", views.contactus_fun, name="contact"),
    path("", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
]
