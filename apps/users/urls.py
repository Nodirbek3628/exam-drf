from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegisterView,
    MeView,
    PatientProfileView,
    UserListView,
    UserDeatilView,
    UserDeleteView,
)

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/me/", MeView.as_view(), name="auth-me"),
    path("patient/profile/", PatientProfileView.as_view(), name="patent-profile"),
    path("users/", UserListView.as_view(), name="userlist"),
    path("users/<int:id>/", UserDeatilView.as_view(), name="users-detail"),
    path("users/<int:id>/delete/", UserDeleteView.as_view(), name="user-delete"),
]
