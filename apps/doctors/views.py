from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import DoctorProfile
from apps.users.permissions import IsOwner

from .serializer import DoctorListSeralizer


class DoctorsListView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request: Request) -> Response:
        doctors = DoctorProfile.objects.all()
        serializer = DoctorListSeralizer(doctors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
