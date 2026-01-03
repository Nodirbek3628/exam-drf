from rest_framework.permissions import BasePermission



class IsAdmin(BasePermission):
    message = 'Siz Admin emassiz'

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin
        )


class IsDoctor(BasePermission):
    message = 'Siz Doctor emassiz'

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_doctor
        )


class IsPatient(BasePermission):
    message = 'Siz Bemor emassiz'

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_patient
            and hasattr(request.user, 'patient_profile')
        )
