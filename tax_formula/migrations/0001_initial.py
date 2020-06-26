# Generated by Django 2.2.8 on 2020-06-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxSlabs2019',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slab1', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slab2', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slab3', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slab4', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slab5', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slab6', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slab7', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slab8', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slab1_basic_deduction', models.IntegerField()),
                ('slab1_percentage_deduction', models.IntegerField()),
            ],
        ),
    ]