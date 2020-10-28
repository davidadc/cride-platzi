"""Users URLs."""

# Django
from django.urls import path

# Views
from cride.users.views import (
    UserLoginAPIView,
    UserSignUpAPIView
)

urlpatterns = [
    path(
        route='login/',
        view=UserLoginAPIView.as_view(),
        name='login',
    ),
    path(
        route='signup/',
        view=UserSignUpAPIView.as_view(),
        name='signup',
    ),
]
