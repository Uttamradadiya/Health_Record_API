from django.contrib.auth.models import AbstractUser
from django.db import models

#This model extends Django's built-in `AbstractUser` to introduce a `role` field. This determines whether a user is a **doctor** or a **patient**. 
# Role-based access is then enforced throughout the app.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PATIENT', 'Patient'),
        ('DOCTOR', 'Doctor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)