from django.contrib import admin
from .models import Machine, MachineType, Manufacturer


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'machine_type', 'model', 'serial_number', 'vintage', 'software_version', 'voltage', 'hours', 'servo', 'firmware', 'customer', 'additional_information', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'manufacturer', 'machine_type', 'model', 'serial_number', 'vintage', 'software_version', 'voltage', 'hours', 'servo', 'firmware', 'customer', 'additional_information', 'is_active', 'created_at', 'updated_at')
    list_filter = ('manufacturer', 'machine_type', 'model', 'serial_number', 'vintage', 'software_version', 'voltage', 'hours', 'servo', 'firmware', 'customer', 'additional_information', 'is_active', 'created_at', 'updated_at')
    search_fields = ('id', 'manufacturer', 'machine_type', 'model', 'serial_number', 'vintage', 'software_version', 'voltage', 'hours', 'servo', 'firmware', 'customer', 'additional_information', 'is_active', 'created_at', 'updated_at')
    list_per_page = 25


@admin.register(MachineType)
class MachineTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    list_per_page = 25


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    list_per_page = 25
