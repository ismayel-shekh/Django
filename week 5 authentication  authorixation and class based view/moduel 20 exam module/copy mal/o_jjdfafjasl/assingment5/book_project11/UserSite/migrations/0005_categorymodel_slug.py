# Generated by Django 4.2.6 on 2024-01-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSite', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
