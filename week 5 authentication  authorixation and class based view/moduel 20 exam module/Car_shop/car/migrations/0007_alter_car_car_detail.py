# Generated by Django 4.2.4 on 2024-01-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_car_car_detail_car_car_quentiry_alter_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_detail',
            field=models.TextField(),
        ),
    ]
