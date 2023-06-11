from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, status

from utils.auth import BearerTokenAuthentication
from .models import Machine, Manufacturer, MachineType
from .serializers import MachineSerializer, ManufacturerSerializer, \
    MachineTypeSerializer, CreateMachineSerializer


class MachineViewSet(ModelViewSet):
    queryset = Machine.objects.filter(is_active=True).order_by("-created_at")
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = MachineSerializer

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
        return Response(self.serializer_class(machine).data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def update(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        if "customer" in data and not user.is_superuser:
            data["customer"] = user.customer.id

        instance = self.get_object()
        serializer = CreateMachineSerializer(instance, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        machine = serializer.save()

        return Response(self.serializer_class(machine).data)

    def get_queryset(self):
        request = self.request
        user = request.user
        queryset = self.queryset

        if user.is_superuser:
            return queryset

        return queryset.filter(customer=user.customer)


class ManufacturerViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Manufacturer.objects.filter(is_active=True).order_by("-created_at")
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = ManufacturerSerializer


class MachineTypeViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = MachineType.objects.filter(is_active=True).order_by("-created_at")
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = MachineTypeSerializer
