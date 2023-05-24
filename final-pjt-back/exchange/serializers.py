from rest_framework import serializers
from .models import ExchangeRateInfo

class ExchangeRateSerializer (serializers.ModelSerializer):
  class Meta:
    model = ExchangeRateInfo
    fields = '__all__'