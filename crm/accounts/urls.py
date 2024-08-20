from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_done'), 
        template_name="accounts/password_reset.html"
        ), name='password_reset'),

    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_sent.html"
        ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete'),
        template_name="accounts/password_reset_form.html"
        ), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_done.html"
        ), name='password_reset_complete'),

    path('', views.home, name='home'),
    path('user', views.userPage, name='userPage'),

    path('account/', views.accountSettings, name='account'),

    path('products', views.products, name='products'),
    path('customers/<str:pk>', views.customers, name='customers'),

    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order')
]