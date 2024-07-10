from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),

    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup_view, name='signup')
]