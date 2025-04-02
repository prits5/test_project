import uuid
from datetime import datetime

from django.db import models

from contract.models import Contract
from product.models import Product


class CreditApplication(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name="credit_application",
    )
    products = models.ManyToManyField(
        Product,
        related_name="credit_applications",
    )
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Credit {self.id}"

    class Meta:
        verbose_name = 'Кредитная заявка'
        verbose_name_plural = 'Кредитные заявки'
