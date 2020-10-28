"""Users URLs."""

# Django
from django.urls import path

# Views
from cride.users.views import (
    UserLoginAPIView,
)

urlpatterns = [
    path(
        route='login/',
        view=UserLoginAPIView.as_view(),
        name='login',
    ),
]
