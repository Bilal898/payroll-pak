# Generated by Django 2.2.8 on 2020-06-26 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_formula', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab2_basic_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab2_percentage_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab3_basic_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab3_percentage_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab4_basic_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab4_percentage_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab5_basic_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab5_percentage_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab6_basic_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab6_percentage_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab7_basic_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab7_percentage_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab8_basic_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taxslabs2019',
            name='slab8_percentage_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab1_basic_deduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab1_percentage_deduction',
            field=models.IntegerField(null=True),
        ),
    ]
