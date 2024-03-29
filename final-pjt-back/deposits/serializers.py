from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    # fin_prdt_cd = serializers.IntegerField(read_only=True)

    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)


class DepositOptionsProductsSerializer(serializers.ModelSerializer):
    # fin_prdt_cd = serializers.IntegerField(read_only=True)
    fin_prdt_cd = DepositProductsSerializer()

    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)