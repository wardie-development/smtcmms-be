# Generated by Django 4.2.2 on 2023-07-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("machine", "0008_machine_hour_active_machine_life_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="other_parts_replaced",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="report",
            name="parts_to_be_replaced_at_the_next_visit",
            field=models.TextField(blank=True, null=True),
        ),
    ]
