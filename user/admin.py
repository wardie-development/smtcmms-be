from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import UserModel
from django.contrib.auth.models import Group


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("id",)
    readonly_fields = ("id",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "username",
                    "email",
                    "password",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "customer",
                )
            },
        ),
    )

    def save_model(self, _, obj, form, change):
        initial_password = form.initial.get("password")
        modified_password = obj.password
        has_password_modified = initial_password != modified_password

        if not change or has_password_modified:
            obj.password = make_password(obj.password)
        obj.save()


admin.site.unregister(Group)
