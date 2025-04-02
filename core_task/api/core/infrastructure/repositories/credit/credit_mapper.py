from api.core.domain.entities import ProductEntity, ContractEntity, ManufacturerEntity
from api.core.domain.entities.credit_application import CreditApplicationEntity
from credit_application.models import CreditApplication


class CreditApplicationMapper:
    @staticmethod
    def to_entity(model: CreditApplication) -> CreditApplicationEntity:
        return CreditApplicationEntity(
            id=model.id,
            contract=ContractEntity(
                id=model.contract.id,
                name=model.contract.name,
            ),
            products=[
                ProductEntity(
                    id=product.id,
                    name=product.name,
                    manufacturer=ManufacturerEntity(
                        id=product.manufacturer.id,
                        name=product.manufacturer.name,
                    ),
                )
                for product in model.products.all()
            ],
        )
