import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List

from credit_application.models import CreditApplication
from .contract import ContractEntity
from .product import ProductEntity


@dataclass
class CreditApplicationEntity:
    id: uuid
    contract: ContractEntity
    products: List[ProductEntity]

    def __str__(self):
        return f"Credit App {self.id} for {self.contract}"
