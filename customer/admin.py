from django.contrib import admin

from .models import Customer, State


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("id",)
    readonly_fields = ("id",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "name",
                )
            },
        ),
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "contact_name",
        "address",
        "phone",
        "city",
        "state",
        "postal_code",
    )
    list_filter = (
        "name",
        "contact_name",
        "address",
        "phone",
        "city",
        "state",
        "postal_code",
    )
    search_fields = (
        "name",
        "contact_name",
        "address",
        "phone",
        "city",
        "state",
        "postal_code",
    )
    ordering = ("id",)
    readonly_fields = ("id",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "name",
                    "contact_name",
                    "address",
                    "phone",
                    "city",
                    "state",
                    "postal_code",
                )
            },
        ),
    )
