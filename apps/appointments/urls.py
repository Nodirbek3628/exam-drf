from django.urls import path
from .views import (
    TimeSlotCreateView,
    TimeSlotDetailView,
    AppointmentsBookingView,
)


urlpatterns = [
    path("timeslots/", TimeSlotCreateView.as_view(), name="timeslot"),
    path("timeslots/<int:id>/", TimeSlotDetailView.as_view(), name="timeslot-detail"),
    path(
        "appointments/", AppointmentsBookingView.as_view(), name="appointment-booking"
    ),
]
