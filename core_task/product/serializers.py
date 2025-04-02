from rest_framework import serializers

from manufacturer.serializers import ManufacturerSerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "manufacturer", "created_at"]
