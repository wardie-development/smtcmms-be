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
    attachment_type = serializers.SerializerMethodField()

    class Meta:
        model = Machine
        fields = "__all__"

    def get_attachment_type(self, obj):
        return obj.attachment_type


class CreateMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"
        extra_kwargs = {"is_active": {"read_only": True}}


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
        extra_kwargs = {"is_active": {"read_only": True}}


class ListReportSerializer(serializers.ModelSerializer):
    machine = MachineSerializer()
    attachment_type = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = "__all__"
        depth = 1

    def get_attachment_type(self, obj):
        return obj.attachment_type
