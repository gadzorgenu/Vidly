# Generated by Django 2.1 on 2021-08-04 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
