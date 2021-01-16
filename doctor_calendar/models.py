from django.db import models
import calendar
from _datetime import datetime, timedelta


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



class Doctor(models.Model):
    doctor_name = models.CharField(max_length=40)
    registration_date = models.DateTimeField("date registered")
    start_of_work = models.TimeField()
    end_of_work = models.TimeField()
    visit_time = models.TimeField()

    # def check_free_slots(self, start_work, end_work, visit_time):
    #     slots = []
    #     slot_start_time = Doctor.start_of_work
    #     while slot_start_time < Doctor.end_of_work:
    #         slot_end_point = slot_start_time.timedelta
    #         slot = {'slot_start_point': slot_start_time, 'slot_end_point': slot_end_point}
    #         slot_start_time += visit_time
    #         if slot in booked_slots: #dopisać listę zarezerwowanych terminów
    #             continue
    #         slots.append(slot)


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField("date registered")
    waiting_status = models.BooleanField()

    @property
    def is_waiting(self):
        return bool(self.waiting_status)
