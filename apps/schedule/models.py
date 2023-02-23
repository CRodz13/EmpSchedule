from django.conf import settings
from django.db import models


class Schedule(models.Model):
    BIWEEKLY_SCHEDULE_CHOICES = [
        ('A', 'Biweekly Schedule A'),
        ('B', 'Biweekly Schedule B'),
    ]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    biweekly_schedule = models.CharField(
        max_length=1,
        choices=BIWEEKLY_SCHEDULE_CHOICES,
        default='A',
    )

    def __str__(self):
        return f"{self.user} - {self.date}"
