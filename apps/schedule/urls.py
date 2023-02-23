from django.urls import path

from .views import (
    schedule_entry_view,
    schedule_list_view,
    schedule_detail_view
)

app_name = "schedules"

urlpatterns = [
    path("schedule_entry/", view=schedule_entry_view, name="schedule_entry"),
    path("schedule_list/", view=schedule_list_view, name="schedule_list"),
    path("schedule/<int:pk>/", view=schedule_detail_view, name="schedule_detail"),
]
