from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, status

from utils.auth import BearerTokenAuthentication
from .models import Machine, Manufacturer, MachineType, Report
from .serializers import (
    MachineSerializer,
    ManufacturerSerializer,
    MachineTypeSerializer,
    CreateMachineSerializer,
    ReportSerializer,
    ListReportSerializer,
)


class MachineViewSet(ModelViewSet):
    queryset = Machine.objects.filter(is_active=True).order_by("-created_at")
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = MachineSerializer

    def list(self, request, *args, **kwargs):
        need_maintenance = request.query_params.get("need_maintenance", None)

        if need_maintenance is not None:
            queryset = self.get_queryset()
            filtered_queryset = []

            for machine in queryset:
                need_maintenance, _, _ = machine.need_maintenance

                if need_maintenance:
                    filtered_queryset.append(machine)

            serializer = self.get_serializer(filtered_queryset, many=True)

            return Response(serializer.data)

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        if user.is_superuser and "customer" not in data:
            raise ValidationError({"error": "Customer is required"})
        elif not user.is_superuser:
            data["customer"] = user.customer.id

        serializer = CreateMachineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        machine = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            self.serializer_class(machine).data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def update(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        if "customer" in data and not user.is_superuser:
            data["customer"] = user.customer.id

        instance = self.get_object()
        serializer = CreateMachineSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        machine = serializer.save()

        return Response(self.serializer_class(machine).data)

    def get_queryset(self):
        request = self.request
        user = request.user
        queryset = self.queryset

        if user.is_superuser:
            return queryset.all()

        return queryset.filter(customer=user.customer)


class ManufacturerViewSet(
    GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = Manufacturer.objects.filter(is_active=True).order_by("-created_at")
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = ManufacturerSerializer


class MachineTypeViewSet(
    GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = MachineType.objects.filter(is_active=True).order_by("-created_at")
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = MachineTypeSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.filter(is_active=True).order_by(
        "-created_at", "-is_verified"
    )
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = ReportSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListReportSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListReportSerializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def machine(self, request, *args, **kwargs):
        machine_id = request.query_params.get("machine_id", None)
        if not machine_id:
            raise ValidationError({"error": "Machine ID is required"})
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(machine_id=machine_id).order_by("created_at")
        serializer = ListReportSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        request = self.request
        user = request.user
        queryset = self.queryset

        if user.is_superuser:
            return queryset.all()

        return queryset.filter(machine__customer=user.customer)
