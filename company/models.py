from django.db import models

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=25)
    company_email = models.CharField(max_length=120)
