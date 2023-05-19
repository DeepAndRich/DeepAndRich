from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.shortcuts import get_object_or_404
from .models import SavingProducts, SavingOptions
from .serializers import SavingProductsSerializer, SavingOptionsSerializer
from django.db.models import Max

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

API_KEY = settings.API_KEY



# Create your views here.
@api_view(['GET'])
def save_saving_products(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(URL, params=params).json()
    # return JsonResponse({'response':response})
    products = response.get('result').get('baseList')
    for product in products:
        product_data = {
            'fin_prdt_cd': product.get('fin_prdt_cd'),
            'kor_co_nm': product.get('kor_co_nm'),
            'fin_prdt_nm': product.get('fin_prdt_nm')
        }
        serializer = SavingProductsSerializer(data=product_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    options = response.get('result').get('optionList')
    for option in options:
        for key in option.keys():
            if option.get(key) is None:
                option[key] = -1
        saving_product = SavingProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
        serializer = SavingOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=saving_product)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def saving_products(request):
    saving_products = SavingProducts.objects.all()
    saving_options = SavingOptions.objects.all()
    products_data = SavingProductsSerializer(saving_products, many=True)
    options_data = SavingOptionsSerializer(saving_options, many=True)
   

    for product in products_data.data:
        product_id = product["id"]
        for option in options_data.data:
          
            if option["fin_prdt_cd"] == product_id:
                matching_options = option
                product.setdefault("deposit_options", []).append(matching_options)
    
    return JsonResponse({
        'saving_products': products_data.data,
    }, json_dumps_params={'ensure_ascii': False})