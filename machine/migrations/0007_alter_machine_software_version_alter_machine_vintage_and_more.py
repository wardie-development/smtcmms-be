# Generated by Django 4.2.2 on 2023-06-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("machine", "0006_alter_machine_attachment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="software_version",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="machine",
            name="vintage",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="machine",
            name="voltage",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
