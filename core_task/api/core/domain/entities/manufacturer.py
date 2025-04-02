import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ManufacturerEntity:
    id: uuid
    name: str

    def __str__(self):
        return self.name
