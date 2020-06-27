from django.db import models
from company.models import Company
# Create your models here.


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=40)
    employee_address = models.CharField(max_length=255)
    employee_email = models.CharField(max_length=40)
    employee_phone = models.CharField(max_length=40)

    def __str__(self):
        return self.employee_name


class EmployeePayrollProfile(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tax_year = models.CharField(
        default=2019, max_length=4, null=True, blank=True)
    monthly_salary = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    yearly_salary = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    medical_allowance = models.FloatField(default=0, blank=True, null=True)
    tax_ded_month = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    net_pay_month = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.employee.employee_name


class EmployeeNetPay(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employeepayrollprofile = models.ForeignKey(
        EmployeePayrollProfile, on_delete=models.CASCADE)
    tax_year = models.CharField(max_length=4)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance_credit = models.FloatField()
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.employee.employee_name
