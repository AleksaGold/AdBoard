# Generated by Django 5.1.3 on 2024-12-05 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="token",
        ),
    ]
