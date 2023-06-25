from django.db import models

from customer.models import Customer
from utils.base.model import BaseModel


class GetAttachmentTypeMixin:
    VIDEO_EXTENSIONS = [
        "mp4",
        "webm",
        "ogg",
        "ogv",
        "avi",
        "mov",
        "wmv",
        "flv",
        "mkv",
    ]

    IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "bmp", "svg", "webp"]

    AUDIO_EXTENSIONS = [
        "mp3",
        "wav",
        "ogg",
        "oga",
        "flac",
        "aac",
        "m4a",
        "wma",
        "alac",
        "aiff",
        "pcm",
        "dsd",
    ]

    @property
    def attachment_type(self):
        attachment = self.attachment

        if attachment.name == "":
            return

        extension = attachment.name.split(".")[-1].lower()

        if extension in self.VIDEO_EXTENSIONS:
            return "video"

        if extension in self.IMAGE_EXTENSIONS:
            return "image"

        if extension in self.AUDIO_EXTENSIONS:
            return "audio"

        return "file"


class Manufacturer(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MachineType(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Machine(GetAttachmentTypeMixin, BaseModel):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    vintage = models.CharField(max_length=255)
    software_version = models.CharField(max_length=255)
    voltage = models.CharField(max_length=255)
    hours = models.CharField(max_length=255, null=True, blank=True)
    servo = models.CharField(max_length=255, null=True, blank=True)
    firmware = models.CharField(max_length=255, null=True, blank=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True
    )

    additional_information = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to="machines", blank=True, null=True)

    def __str__(self):
        return self.model


class Report(GetAttachmentTypeMixin, BaseModel):
    REPORT_TYPE_CHOICES = (
        ("Preventive Maintenance", "Preventive Maintenance"),
        ("Corrective Maintenance", "Corrective Maintenance"),
        ("Commissioning", "Commissioning"),
    )
    machine = models.ForeignKey(
        Machine, on_delete=models.CASCADE, related_name="reports"
    )
    report_type = models.CharField(max_length=255, choices=REPORT_TYPE_CHOICES)
    notes = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    symptoms = models.TextField(blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)
    po = models.CharField(max_length=255, blank=True, null=True)
    attachment = models.FileField(upload_to="reports", blank=True, null=True)

    def __str__(self):
        return self.report_type
