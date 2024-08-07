from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.index_blank, name="index_blank"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),

    path("<str:section>", views.index, name="index"),
    path("sections/<str:section>", views.section, name="section")


]