from django.contrib import admin
from .models import Employee, EmployeePayrollProfile, EmployeeNetPay
# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeePayrollProfile)
admin.site.register(EmployeeNetPay)
