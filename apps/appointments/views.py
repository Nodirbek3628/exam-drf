from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from apps.users.permissions import IsDoctor, IsPatient
from .serializer import TimeSlotCreatSerializer, AppointmentsBookingSerializer
from .models import TimeSlot


class TimeSlotCreateView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def post(self, request: Request) -> Response:
        serializer = TimeSlotCreatSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save(doctor=request.user.doctor_profile, is_available=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        timeslot = TimeSlot.objects.all()
        serializer = TimeSlotCreatSerializer(timeslot, many=True)

        return Response(serializer.data)


class TimeSlotDetailView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request: Request, id: int) -> Response:
        doctor = get_object_or_404(TimeSlot, id=id)
        serializer = TimeSlotCreatSerializer(doctor)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, id: int) -> Response:
        doctor = get_object_or_404(TimeSlot, id=id)
        doctor.delete()

        return Response(
            {"detail": f"{id}-id  Muvafaqiyatli o'chirildi"}, status=status.HTTP_200_OK
        )


class AppointmentsBookingView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def post(self, request: Request) -> Response:
        serializer = AppointmentsBookingSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        appointment = serializer.save()

        return Response(
            {"id": appointment.id, "timeslot": appointment.timeslot.id},
            status=status.HTTP_201_CREATED,
        )
