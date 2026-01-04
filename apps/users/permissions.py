from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = "Siz Admin emassiz"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsDoctor(BasePermission):
    message = "Siz Doctor emassiz"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_doctor


class IsPatient(BasePermission):
    message = "Siz Patient emassiz"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_patient


class IsOwner(BasePermission):
    message = "siz Admin Ham Patient ham emassz"

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_admin or user.is_patient)
