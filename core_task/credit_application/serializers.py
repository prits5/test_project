from rest_framework import serializers

from contract.serializers import ContractSerializer
from credit_application.models import CreditApplication
from product.serializers import ProductSerializer


class CreditApplicationSerializer(serializers.ModelSerializer):
    contract = ContractSerializer()
    products = ProductSerializer(many=True, source="products.all")

    class Meta:
        model = CreditApplication
        fields = ["id", "contract", "products", "created_at"]
