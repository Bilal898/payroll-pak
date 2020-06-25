from django.urls import path
from .views import register, login_view, logout_view

# app_name = 'company'
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view"),
]