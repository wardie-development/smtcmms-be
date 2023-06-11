from django.db import models

from customer.models import Customer
from utils.base.model import BaseModel


class Manufacturer(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MachineType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Machine(BaseModel):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    vintage = models.CharField(max_length=255)
    software_version = models.CharField(max_length=255)
    voltage = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)
    servo = models.CharField(max_length=255)
    firmware = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
