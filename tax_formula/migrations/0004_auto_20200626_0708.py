# Generated by Django 2.2.8 on 2020-06-26 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_formula', '0003_auto_20200626_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab1',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab2',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab3',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab4',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab5',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab6',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab7',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxslabs2019',
            name='slab8',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
