from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from utils.auth import BearerTokenAuthentication
from .models import UserModel
from .permissions import UserPermissions
from .serializers import LoginSerializer, AuthenticatedUserSerializer


class UserViewSet(GenericViewSet):
    queryset = UserModel.objects.all()
    permission_classes = [UserPermissions]
    authentication_classes = [BearerTokenAuthentication]

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user

        user_data = AuthenticatedUserSerializer(user).data

        return Response(user_data)

    @action(detail=False, methods=["get"])
    def data(self, request):
        user = request.user
        serializer = AuthenticatedUserSerializer(user)

        return Response(serializer.data)
