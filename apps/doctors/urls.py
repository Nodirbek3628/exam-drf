from django.urls import path
from .views import DoctorsListView


urlpatterns = [path("doctors/", DoctorsListView.as_view(), name="doctors-list")]
