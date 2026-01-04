from django.db import models
from django.core.exceptions import ValidationError

from apps.doctors.models import DoctorProfile
from apps.users.models import PatientProfile


class TimeSlot(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("doctor", "date", "start_time")

    def __str__(self):
        return f"{self.doctor}|{self.date} {self.start_time}-{self.end_time}"


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        CANCELLED = "CANCELLED", "Cancelled"

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name="appointments"
    )
    timeslot = models.OneToOneField(
        TimeSlot, on_delete=models.CASCADE, related_name="appointment"
    )
    status = models.CharField(max_length=20, choices=Status.choices, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def doctor(self):
        return self.timeslot.doctor
