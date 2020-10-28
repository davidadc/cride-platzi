"""Circles URLs."""

# Django
from django.urls import path

# View
from cride.circles.views import list_circles, create_circle

urlpatterns = [
    path(
        route='',
        view=list_circles,
    ),
    path(
        route='create/',
        view=create_circle,
    )
]
