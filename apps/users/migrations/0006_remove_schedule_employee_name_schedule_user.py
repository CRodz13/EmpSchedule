# Generated by Django 4.1.7 on 2023-02-23 03:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_schedule"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schedule",
            name="employee_name",
        ),
        migrations.AddField(
            model_name="schedule",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]