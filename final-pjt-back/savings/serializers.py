from rest_framework import serializers
from .models import SavingProducts, SavingOptions

class SavingProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavingProducts
        fields = '__all__'



class SavingOptionsSerializer(serializers.ModelSerializer):
    # fin_prdt_cd = serializers.IntegerField(read_only=True)
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)



class SavingOptionsProductsSerializer(serializers.ModelSerializer):
    # fin_prdt_cd = serializers.IntegerField(read_only=True)
    fin_prdt_cd = SavingProductsSerializer()

    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)
