import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ContractEntity:
    id: uuid
    name: str

    def __str__(self):
        return f"Contract {self.name}"
