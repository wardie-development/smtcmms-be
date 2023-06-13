from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from utils.auth import BearerTokenAuthentication
from .models import Customer, State
from .permissions import CustomerPermissions
from .serializers import CustomerSerializer, ListCustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.filter(is_active=True).order_by("-created_at")
    permission_classes = [IsAuthenticated, CustomerPermissions]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = CustomerSerializer

    def get_serializer(self, *args, **kwargs):
        if self.action in ("list", "retrieve"):
            return ListCustomerSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    @action(detail=False, methods=["GET"])
    def states(self, request, *args, **kwargs):
        states = State.objects.all().values("id", "name")
        return Response(states, status=status.HTTP_200_OK)
