from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .forms import ScheduleForm
from .models import Schedule


class ScheduleEntryView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedule_entry.html'
    success_url = reverse_lazy('schedule:list')

schedule_entry_view = ScheduleEntryView.as_view()


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule_list.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset

    def get(self, request, *args, **kwargs):
        print('ListView.get() is being called')
        return super().get(request, *args, **kwargs)


schedule_list_view = ScheduleListView.as_view()


class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedule_detail.html'
    context_object_name = 'schedules'

schedule_detail_view = ScheduleDetailView.as_view()
