# Generated by Django 2.1.2 on 2018-11-04 19:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='dayOfWeek',
            field=models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='dayOfWeek',
            field=models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
