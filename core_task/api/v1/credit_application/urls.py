from django.urls import path

from credit_application.views import CreditApplicationManufacturersViewSet


urlpatterns = [
    path(
        "contract/<uuid:id>/manufacturers/",
        CreditApplicationManufacturersViewSet.as_view({"get": "get_manufacturers"}),
        name="contract-manufacturers",
    ),
]
