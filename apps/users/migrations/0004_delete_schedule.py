# Generated by Django 4.1.7 on 2023-02-20 13:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_schedule_location"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Schedule",
        ),
    ]
