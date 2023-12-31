# Generated by Django 4.2.2 on 2023-06-13 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="State",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="customer.state"
            ),
        ),
    ]
