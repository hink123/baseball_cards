# Generated by Django 2.2.6 on 2019-12-16 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateField(verbose_name='Date Offered'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Bid'),
        ),
    ]