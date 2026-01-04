from rest_framework import serializers
from .models import DoctorProfile
from apps.users.models import CustomUser


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )


class DoctorListDetailSeralizer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)

    class Meta:
        model = DoctorProfile
        fields = (
            "id",
            "specialization",
            "experience_years",
            "gender",
            "user",
        )


class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ("specialization", "experience_years", "gender")
