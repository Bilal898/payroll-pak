# Generated by Django 2.2.8 on 2020-06-21 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20200621_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=255),
        ),
    ]