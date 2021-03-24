# Generated by Django 3.1.7 on 2021-03-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supersub', '0009_auto_20210321_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fatty_acids',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='salt',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='saturated_fatty_acids',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='sugar',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(default=None),
        ),
    ]