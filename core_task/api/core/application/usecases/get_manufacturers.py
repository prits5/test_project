import logging
from uuid import UUID
from typing import List

from api.core.application.exceptions.credit_exceptions import CreditApplicationNotFound
from api.core.application.exceptions.product_exceptions import ProductsNotFoundError
from api.core.application.interfaces.repositories.credit_application_repo import (
    ICreditApplicationRepository,
)

logger = logging.getLogger(__name__)


class GetManufacturersByContractUseCase:
    def __init__(self, repository: ICreditApplicationRepository):
        self.repository = repository
        logger.debug("Initialized UseCase with repository: %s",
                     repository.__class__.__name__)

    def __call__(self, contract_id: UUID) -> List[UUID]:
        logger.info("Starting search for contract: %s", contract_id)

        credit_app = self.repository.get_by_contract_id(contract_id)

        if not credit_app:
            raise CreditApplicationNotFound()

        if not credit_app.products:
            raise ProductsNotFoundError()

        manufacturers = list({p.manufacturer.id for p in credit_app.products})
        logger.info("Found %d unique for contract %s",
                    len(manufacturers),
                    contract_id)

        return manufacturers
