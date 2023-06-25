# Generated by Django 4.2.2 on 2023-06-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("machine", "0004_report_po_report_service_description_report_symptoms"),
    ]

    operations = [
        migrations.AddField(
            model_name="machine",
            name="attachment",
            field=models.FileField(blank=True, null=True, upload_to="reports"),
        ),
        migrations.AddField(
            model_name="report",
            name="attachment",
            field=models.FileField(blank=True, null=True, upload_to="reports"),
        ),
    ]
