# Generated by Django 3.1.5 on 2021-01-17 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_calendar', '0002_doctor_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
