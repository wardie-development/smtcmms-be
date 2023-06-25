from rest_framework import serializers

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
        extra_kwargs = {"is_active": {"read_only": True}}


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
