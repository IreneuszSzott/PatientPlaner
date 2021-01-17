from django.conf.urls import url
from . import views

app_name = 'doctor_calendar'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.CalendarView, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.CalendarView, name='event_edit'),
]
