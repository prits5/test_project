from uuid import UUID

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.core.application.usecases.get_manufacturers import (
    GetManufacturersByContractUseCase,
)
from api.core.infrastructure.repositories.credit.repo import (
    CreditApplicationRepository,
)
from credit_application.models import CreditApplication
from credit_application.serializers import CreditApplicationSerializer


class CreditApplicationManufacturersViewSet(viewsets.ModelViewSet):
    serializer_class = CreditApplicationSerializer
    queryset = CreditApplication.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.manufacturers_usecase = GetManufacturersByContractUseCase(
            repository=CreditApplicationRepository()
        )

    @action(detail=False, methods=["get"])
    def get_manufacturers(self, request, contract_id: UUID) -> Response:
        manufacturer_ids = self.manufacturers_usecase(contract_id)
        return Response(
            {
                "contract_id": str(contract_id),
                "manufacturer_ids": [str(mid) for mid in manufacturer_ids],
            },
            status=status.HTTP_200_OK,
        )
