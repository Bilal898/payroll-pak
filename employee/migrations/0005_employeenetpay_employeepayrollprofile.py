# Generated by Django 2.2.8 on 2020-06-27 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20200627_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeenetpay',
            name='employeepayrollprofile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.EmployeePayrollProfile'),
            preserve_default=False,
        ),
    ]
