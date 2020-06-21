from django.db import models
from company.models import Company
# Create your models here.


class Employee(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.TextField()
    employee_address = models.TextField()
    employee_email = models.TextField()
    employee_phone = models.TextField()


class EmployeePayrollProfile(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tax_year = models.CharField(max_length=4)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance = models.FloatField()
