# Generated by Django 2.2.8 on 2020-06-21 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.TextField()),
                ('employee_address', models.TextField()),
                ('employee_email', models.TextField()),
                ('employee_phone', models.TextField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePayrollProfile2019',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medical_allowance', models.FloatField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
    ]