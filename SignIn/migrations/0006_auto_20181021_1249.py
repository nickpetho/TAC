# Generated by Django 2.1.2 on 2018-10-21 16:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignIn', '0005_auto_20181020_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='comments',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='course',
            field=models.CharField(choices=[('MATH 1505', 'MATH 1505 - INTERMEDIATE ALGEBRA WITH APPS'), ('MATH 1507', 'MATH 1507 - INTERMEDIATE ALGEBRA'), ('MATH 1510', 'MATH 1510 - COLLEGE ALGEBRA'), ('MATH 1511', 'MATH 1511 - TRIGONOMETRY'), ('MATH 1513', 'MATH 1513 - PRE CALCULUS'), ('MATH 1552', 'MATH 1552 - BUSINESS CALCULUS (APPLIED MATH FOR MANAGEMENT)'), ('MATH 2623', 'MATH 2623 - QUANTITATIVE REASONING'), ('MATH 2623H', 'MATH 2623H - HONORS QUANTITATIVE REASONING'), ('MATH 1571', 'MATH 1571 - CALCULUS 1'), ('MATH 1572', 'MATH 1572 - CALCULUS 2'), ('MATH 2673', 'MATH 2673 - CALCULUS 3'), ('MATH 1570', 'MATH 1570 - APPLIED CALCULUS 1'), ('MATH 2670', 'MATH 2670 - APPLIED CALCULUS 2'), ('MATH 2651', 'MATH 2651 - MATH FOR EARLY CHILDHOOD TEACHERS 1'), ('MATH 2652', 'MATH 2652 - MATH FOR EARLY CHILDHOOD TEACHERS 2'), ('MATH 1564', 'MATH 1564 - FOUNDATIONS OF MIDDLE SCHOOL MATH 1'), ('MATH 2665', 'MATH 2665 - FOUNDATIONS OF MIDDLE SCHOOL MATH 2'), ('MATH 1585H', 'MATH 1585H - ACCELERATED HONORS CALCULUS 1'), ('MATH 2686H', 'MATH 2686H - ACCELERATED HONORS CALCULUS 2'), ('MATH 1571H', 'MATH 1571H - HONORS CALCULUS 1'), ('MATH 1586H', 'MATH 1586H - HONORS CALCULUS 1 LAB'), ('MATH 1572H', 'MATH 1572H - HONORS CALCULUS 2'), ('MATH 2687H', 'MATH 2687H - HONORS CALCULUS 2 LAB'), ('MATH 2673H', 'MATH 2673H - HONORS CALCULUS 3'), ('MATH 1580H', 'MATH 1580H - HONORS BIOMATHEMATICS 1'), ('MATH 1581H', 'MATH 1581H - HONORS BIOMATHEMATICS 2'), ('MATH 3705', 'MATH 3705 - DIFFERENTIAL EQUATIONS'), ('MATH 3705H', 'MATH 3705H - HONORS DIFFERENTIAL EQUATIONS'), ('MATH 3715', 'MATH 3715 - DISCRETE MATHEMATICS'), ('MATH 3720', 'MATH 3720 - LINEAR ALGEBRA'), ('MATH 3715', 'MATH 3715 - DISCRETE MATHEMATICS'), ('STAT 2601', 'STAT 2601 - INTRODUCTORY STATISTICS'), ('STAT 2625', 'STAT 2625 - STATISTICS LITERACY & CRITICAL REASONING'), ('STAT 3717', 'STAT 3717 - STATISTICAL METHODS'), ('STAT 3743', 'STAT 3743 - PROBABILITY AND STATISTICS'), ('OTHER', 'OTHER - OTHER COURSE NOT LISTED')], max_length=50, verbose_name='Course Seeking Help For'),
        ),
        migrations.AlterField(
            model_name='session',
            name='endTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]