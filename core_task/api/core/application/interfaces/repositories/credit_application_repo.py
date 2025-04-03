from typing import Protocol
from uuid import UUID

from api.core.domain.entities.credit_application import CreditApplicationEntity


class ICreditApplicationRepository(Protocol):
    @staticmethod
    def get_by_contract_id(contract_id: UUID) -> CreditApplicationEntity:
        pass
