# Generated by Django 4.2.6 on 2024-01-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSite', '0007_alter_postmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='Book_Quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
