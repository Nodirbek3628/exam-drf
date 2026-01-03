from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializer import (
    RegisterSeializer,
    UserSerializer,
    MeSerializer,
    PatientProfileSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserUpdateSeralizer,
)
from .permissions import IsPatient, IsAdmin
from apps.users.models import CustomUser


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = RegisterSeializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            user_json = UserSerializer(user).data

            return Response(user_json, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        serializer = MeSerializer(request.user)
        return Response(serializer.data)


class PatientProfileView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def get(self, request):
        profile = request.user.patient_profile
        serializer = PatientProfileSerializer(profile)
        return Response(serializer.data)

    def patch(self, request):
        profile = request.user.patient_profile
        serializer = PatientProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request: Request) -> Response:
        users = CustomUser.objects.all()
        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)


class UserDeatilView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request: Request, id: int) -> Response:
        user = get_object_or_404(CustomUser, id=id)
        serializer = UserDetailSerializer(user)

        return Response(serializer.data)

    def patch(self, request: Request, id: int) -> Response:
        user = get_object_or_404(CustomUser, id=id)
        serializer = UserUpdateSeralizer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteView(APIView):
    def delete(self, request: Request, id: int) -> Response:
        user = get_object_or_404(CustomUser, id=id)
        user.delete()

        return Response(
            {"detail": f"{id}-User muvafaqiyatli o'chirildi "},
            status=status.HTTP_204_NO_CONTENT,
        )
