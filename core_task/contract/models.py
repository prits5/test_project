import uuid
from datetime import datetime

from django.db import models

from mixins.models import BaseModelMixin


class Contract(BaseModelMixin):
    name: str = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'
