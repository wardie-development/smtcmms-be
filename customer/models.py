from django.db import models

from utils.base.model import BaseModel


class State(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Customer(BaseModel):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
