from django.urls import path
from .views import DoctorsListView, DoctorDetailView, DoctorProfileView


urlpatterns = [
    path("doctors/", DoctorsListView.as_view(), name="doctors-list"),
    path("doctors/<int:id>/", DoctorDetailView.as_view(), name="doctor-detail"),
    path("doctor/profile/", DoctorProfileView.as_view(), name="doctor-profile"),
]
