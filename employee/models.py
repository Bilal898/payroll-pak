from django.db import models
from company.models import Company
# Create your models here.


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=40)
    employee_address = models.CharField(max_length=255)
    employee_email = models.CharField(max_length=40)
    employee_phone = models.CharField(max_length=40)


class EmployeePayrollProfile(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tax_year = models.CharField(max_length=4)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance = models.FloatField()


class EmployeeNetPay(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tax_year = models.CharField(max_length=4)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance_credit = models.FloatField()
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
