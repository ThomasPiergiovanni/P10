# Generated by Django 3.1.7 on 2021-04-10 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_origin', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_origin', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('nutriscore_grade', models.CharField(max_length=8)),
                ('fat', models.DecimalField(decimal_places=3, max_digits=8)),
                ('saturated_fat', models.DecimalField(decimal_places=3, max_digits=8)),
                ('sugar', models.DecimalField(decimal_places=3, max_digits=8)),
                ('salt', models.DecimalField(decimal_places=3, max_digits=8)),
                ('image', models.URLField()),
                ('url', models.URLField()),
                ('categories', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supersub.category')),
                ('relation_user', models.ManyToManyField(through='supersub.Favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='favorites',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supersub.product'),
        ),
    ]
