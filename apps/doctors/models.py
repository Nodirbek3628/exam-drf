from django.db import models
from apps.users.models import CustomUser


class DoctorProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="doctor_profile"
    )
    specialization = models.CharField(max_length=128)
    experience_years = models.PositiveSmallIntegerField(default=0)
    gender = models.CharField(
        max_length=10, choices=Gender.choices, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username} ({self.specialization})"
