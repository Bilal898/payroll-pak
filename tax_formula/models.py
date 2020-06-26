from django.db import models

# Create your models here.


class TaxSlabs2019(models.Model):
    slab1 = models.DecimalField(max_digits=9, decimal_places=2)
    slab1_basic_deduction = models.IntegerField(null=True)
    slab1_percentage_deduction = models.IntegerField(null=True)

    slab2 = models.DecimalField(max_digits=9, decimal_places=2)
    slab2_basic_deduction = models.IntegerField(null=True)
    slab2_percentage_deduction = models.IntegerField(null=True)

    slab3 = models.DecimalField(max_digits=9, decimal_places=2)
    slab3_basic_deduction = models.IntegerField(null=True)
    slab3_percentage_deduction = models.IntegerField(null=True)

    slab4 = models.DecimalField(max_digits=9, decimal_places=2)
    slab4_basic_deduction = models.IntegerField(null=True)
    slab4_percentage_deduction = models.IntegerField(null=True)

    slab5 = models.DecimalField(max_digits=9, decimal_places=2)
    slab5_basic_deduction = models.IntegerField(null=True)
    slab5_percentage_deduction = models.IntegerField(null=True)

    slab6 = models.DecimalField(max_digits=9, decimal_places=2)
    slab6_basic_deduction = models.IntegerField(null=True)
    slab6_percentage_deduction = models.IntegerField(null=True)

    slab7 = models.DecimalField(max_digits=9, decimal_places=2)
    slab7_basic_deduction = models.IntegerField(null=True)
    slab7_percentage_deduction = models.IntegerField(null=True)

    slab8 = models.DecimalField(max_digits=9, decimal_places=2)
    slab8_basic_deduction = models.IntegerField(null=True)
    slab8_percentage_deduction = models.IntegerField(null=True)
