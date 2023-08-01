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
    maintenance = serializers.SerializerMethodField()

    class Meta:
        model = Machine
        fields = "__all__"

    def get_attachment_type(self, obj):
        return obj.attachment_type

    def get_maintenance(self, obj):
        need_maintenance, next_maintenance_datetime, days_until_next_maintenance = obj.need_maintenance
        next_maintenance_datetime_json = None
        if next_maintenance_datetime:
            next_maintenance_datetime_json = (
                next_maintenance_datetime.strftime("%Y-%m-%dT%H:%M:%S")
            )
        if days_until_next_maintenance:
            days_until_next_maintenance = days_until_next_maintenance.days

        return {
            "need_maintenance": need_maintenance,
            "next_maintenance_datetime": next_maintenance_datetime_json,
            "days_until_next_maintenance": days_until_next_maintenance
        }


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
