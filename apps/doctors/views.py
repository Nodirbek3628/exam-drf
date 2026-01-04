from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import DoctorProfile
from apps.users.permissions import IsOwner, IsDoctor

from .serializer import DoctorListDetailSeralizer, DoctorUpdateSerializer


class DoctorsListView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request: Request) -> Response:
        doctors = DoctorProfile.objects.all()
        serializer = DoctorListDetailSeralizer(doctors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request: Request, id: int) -> Response:
        doctor = get_object_or_404(DoctorProfile, id=id)
        serializer = DoctorListDetailSeralizer(doctor)

        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorProfileView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request: Request) -> Response:
        profile = get_object_or_404(DoctorProfile, user=request.user)
        serializer = DoctorListDetailSeralizer(profile)

        return Response(serializer.data)

    def patch(self, request: Request) -> Response:
        profile = get_object_or_404(DoctorProfile, user=request.user)
        serializer = DoctorUpdateSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
