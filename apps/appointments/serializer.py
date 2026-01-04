from rest_framework import serializers
from .models import TimeSlot, Appointment


class TimeSlotCreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ("id", "date", "start_time", "end_time")

    def validate(self, attrs):
        if attrs["end_time"] <= attrs["start_time"]:
            raise serializers.ValidationError(
                {"end_time": "End time start time dan katta bullishi kerak."}
            )
        return super().validate(attrs)


class AppointmentsBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("timeslot",)

    def validate_timeslot(self, value):
        if hasattr(value, "appointment"):
            raise serializers.ValidationError("Bu time slot allaqachon band.")
        if not value.is_available:
            raise serializers.ValidationError("Bu slot mavjud emas.")
        return value

    def create(self, validated_data):
        patient = self.context["request"].user.patientprofile
        timeslot = validated_data["timeslot"]

        doctor = timeslot.doctor

        timeslot.is_available = False
        timeslot.save()

        return Appointment.objects.create(
            doctor=doctor, patient=patient, timeslot=timeslot
        )
