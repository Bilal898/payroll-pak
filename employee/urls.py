from django.contrib import admin
from django.urls import path
from .views import employee_create_view

# app_name = 'employee'
urlpatterns = [
    path('create/', employee_create_view, name="employee_create"),
    # path('dashboard/', employee_dashboard_view, name="employee_dashboard"),
]
