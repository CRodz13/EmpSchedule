# Generated by Django 4.1.7 on 2023-02-23 04:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_alter_schedule_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Schedule",
        ),
    ]