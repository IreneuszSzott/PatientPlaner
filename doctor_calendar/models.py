from django.db import models
from django.contrib import admin


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time']

