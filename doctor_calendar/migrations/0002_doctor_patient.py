# Generated by Django 3.1.5 on 2021-01-16 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_calendar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=40)),
                ('registration_date', models.DateTimeField(verbose_name='date registered')),
                ('start_of_work', models.TimeField()),
                ('end_of_work', models.TimeField()),
                ('visit_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('registration_date', models.DateTimeField(verbose_name='date registered')),
                ('waiting_status', models.BooleanField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_calendar.doctor')),
            ],
        ),
    ]