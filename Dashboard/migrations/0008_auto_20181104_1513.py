# Generated by Django 2.1.2 on 2018-11-04 20:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0007_auto_20181104_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='dayOfWeek',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='dayOfWeek',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterUniqueTogether(
            name='availability',
            unique_together={('user', 'dayOfWeek')},
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('user', 'dayOfWeek')},
        ),
    ]
