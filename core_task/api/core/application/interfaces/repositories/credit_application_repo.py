from typing import Protocol
from uuid import UUID

from api.core.domain.entities.credit_application import CreditApplicationEntity


class ICreditApplicationRepository(Protocol):
    def get_by_contract_id(self, contract_id: UUID) -> CreditApplicationEntity:
        pass
