import uuid
from datetime import datetime

from django.db import models

from contract.models import Contract
from mixins.models import BaseModelMixin
from product.models import Product


class CreditApplication(BaseModelMixin):
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name="credit_application",
    )

    def __str__(self):
        return f"Credit {self.id}"

    class Meta:
        verbose_name = 'Кредитная заявка'
        verbose_name_plural = 'Кредитные заявки'
