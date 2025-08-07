from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Driver"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.OneToOneField(
        "Manufacturer", unique=True, on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(Driver)

    def __str__(self):
        return self.model


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} (country: {self.country})"
