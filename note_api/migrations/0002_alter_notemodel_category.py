# Generated by Django 4.2.6 on 2023-10-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("note_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notemodel",
            name="category",
            field=models.CharField(max_length=255),
        ),
    ]
