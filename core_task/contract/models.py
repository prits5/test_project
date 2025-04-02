import uuid
from datetime import datetime

from django.db import models


class Contract(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name: str = models.CharField(max_length=255)
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'
