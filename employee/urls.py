from django.contrib import admin
from django.urls import path
from .views import employee_create_view, employee_process_payroll

app_name = 'employee'
urlpatterns = [
    path('create/', employee_create_view, name="employee_create"),
    path('process_payroll/', employee_process_payroll, name="process_payroll"),
    # path('dashboard/', employee_dashboard_view, name="employee_dashboard"),
]
