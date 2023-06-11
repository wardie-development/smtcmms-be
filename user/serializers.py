from django.utils import timezone

from .models import UserModel
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError


class LoginSerializer(serializers.Serializer):
    user = None

    username = serializers.CharField()
    password = serializers.CharField()

    @staticmethod
    def _validate_password(password, password_to_check):
        is_valid_password = check_password(password, password_to_check)

        if not is_valid_password:
            raise UserModel.DoesNotExist

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        try:
            user = UserModel.objects.only("password", "username", "last_login").get(
                username=username
            )
            user.last_login = timezone.now()
            user.save()

            self.user = user

            self._validate_password(password, user.password)

        except UserModel.DoesNotExist:
            raise ValidationError({"error": "Invalid username or password"})

        return data


class AuthenticatedUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserModel
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "token",
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
            "last_login",
        ]

    @staticmethod
    def get_token(obj):
        token, _ = Token.objects.get_or_create(user=obj)

        return token.key
