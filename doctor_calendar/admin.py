from django.contrib import admin
from doctor_calendar.models import Event

admin.site.register(Event)


class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time']

