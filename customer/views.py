from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from utils.auth import BearerTokenAuthentication
from .models import Customer
from .permissions import CustomerPermissions
from .serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.filter(is_active=True).order_by("-created_at")
    permission_classes = [IsAuthenticated, CustomerPermissions]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = CustomerSerializer
