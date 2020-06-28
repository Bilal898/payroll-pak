from django.contrib import admin
from django.urls import path
from .views import (employee_create_view, employee_process_payroll, calculate_pay,
                    list_employees_view, calculate_pay_profile, employee_payroll_profile_view)

app_name = 'employee'
urlpatterns = [
    path('create/', employee_create_view, name="employee_create"),
    path('process_payroll/', employee_process_payroll, name="process_payroll"),
    path('calculate_pay/', calculate_pay, name="calculate_pay"),
    path('calculate_pay_profile/', calculate_pay_profile,
         name="calculate_pay_profile"),
    path('list_employees/', list_employees_view, name="list_employees"),
    # path('setup_payroll/',
    #      employee_payroll_profile_view, name="setup_payroll"),
    path('<int:employee_id>/payroll_profile/',
         employee_payroll_profile_view, name="payroll_profile"),
    # path('dashboard/', employee_dashboard_view, name="employee_dashboard"),
]
