from rest_framework.serializers import ModelSerializer
from .models import *

class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceDetailSerializer(ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'