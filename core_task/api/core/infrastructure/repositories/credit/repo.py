import logging
from uuid import UUID

from django.core.exceptions import ObjectDoesNotExist

from api.core.application.interfaces.repositories.credit_application_repo import (
    ICreditApplicationRepository,
)
from api.core.domain.entities.credit_application import CreditApplicationEntity
from api.core.infrastructure.repositories.credit.credit_mapper import (
    CreditApplicationMapper,
)
from credit_application.models import CreditApplication

logger = logging.getLogger(__name__)


class CreditApplicationRepository:
    @staticmethod
    def get_by_contract_id(contract_id: UUID) -> CreditApplicationEntity | None:
        logger.debug(
            "Starting to fetch for contract ID: %s",
            contract_id
        )

        try:
            credit_app = (
                CreditApplication.objects.select_related("contract")
                .prefetch_related("products", "products__manufacturer")
                .get(contract__id=contract_id)
            )

            logger.debug("Full credit app data: %s", credit_app.__dict__)

            return CreditApplicationMapper.to_entity(credit_app)
        except (CreditApplication.DoesNotExist, ObjectDoesNotExist):
            logger.warning(
                "Credit application not found for contract ID: %s",
                contract_id
            )
            return None
