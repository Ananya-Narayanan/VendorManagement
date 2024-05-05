from rest_framework import serializers
from vendorapp.models import vendor,purchaseorder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=purchaseorder
        fields='__all__'