# Generated by Django 5.1.7 on 2025-04-03 16:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contract", "0001_initial"),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CreditApplication",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата обновления."
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания."
                    ),
                ),
                (
                    "contract",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credit_application",
                        to="contract.contract",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="credit_applications", to="product.product"
                    ),
                ),
            ],
            options={
                "verbose_name": "Кредитная заявка",
                "verbose_name_plural": "Кредитные заявки",
            },
        ),
    ]
