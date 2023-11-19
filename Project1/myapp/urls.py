from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.welcome, name="welcome"),
    path("about/", views.about_fun, name="about"),
    path("contactus/", views.contactus_fun, name="contact"),
    path("", views.login_view, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("signup/", views.signup_view, name="signup"),
]
