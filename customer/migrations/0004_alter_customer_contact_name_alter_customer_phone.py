# Generated by Django 4.2.2 on 2023-08-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0003_alter_customer_postal_code_alter_customer_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="contact_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
