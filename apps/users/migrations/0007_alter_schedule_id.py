# Generated by Django 4.1.7 on 2023-02-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_remove_schedule_employee_name_schedule_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
