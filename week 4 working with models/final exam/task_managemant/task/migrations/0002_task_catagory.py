# Generated by Django 4.2.4 on 2024-01-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_catagory_task'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='catagory',
            field=models.ManyToManyField(to='category.catagory'),
        ),
    ]