from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView, LogoutView, PasswordResetView, PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from . import views
import EnCasDeSoif.views as ec
urlpatterns = [
    path('', ec.index),
    path('login/', views.login_user, name="login"),
    path('logout/', views.view_logout, name='logout'),
    path('register/', views.register, name="register"),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),

]
