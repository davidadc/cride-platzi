"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """User model.

    Extends from Django's Abstract User, change the username field to email and
    add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_message={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_number = models.CharField(
        max_length=17,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verifier = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address. '
    )
