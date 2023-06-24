from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from customer.models import Customer
from customer.serializers import CustomerSerializer
from .models import Machine, Manufacturer, MachineType, Report


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class MachineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineType
        fields = "__all__"


class MachineSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    machine_type = MachineTypeSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Machine
        fields = "__all__"


class CreateMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class ListReportSerializer(serializers.ModelSerializer):
    machine = MachineSerializer()

    class Meta:
        model = Report
        fields = "__all__"
        depth = 1
