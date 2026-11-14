from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Administrator"
        STUDENT = "student", "Student"
        FACILITATOR = "facilitator", "Facilitator"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT)