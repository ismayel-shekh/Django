# Generated by Django 4.2.4 on 2024-01-16 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_car_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_type',
        ),
    ]
