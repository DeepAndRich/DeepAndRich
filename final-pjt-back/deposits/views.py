from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.shortcuts import get_object_or_404
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from django.db.models import Max

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

API_KEY = settings.API_KEY



# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
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
        serializer = DepositProductsSerializer(data=product_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    options = response.get('result').get('optionList')
    for option in options:
        for key in option.keys():
            if option.get(key) is None:
                option[key] = -1
        deposit_product = DepositProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=deposit_product)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def deposit_products(request):
    deposit_products = DepositProducts.objects.all()
    deposit_options = DepositOptions.objects.all()
    products_data = DepositProductsSerializer(deposit_products, many=True)
    options_data = DepositOptionsSerializer(deposit_options, many=True)
    # print(products_data)
    # print('----------------')
    # return JsonResponse({
    # 'deposit_products': products_data.data,
    # 'deposit_options': options_data.data
    # })

    for product in products_data.data:
        product_id = product["id"]
        for option in options_data.data:
          
            if option["fin_prdt_cd"] == product_id:
                matching_options = option
                product.setdefault("deposit_options", []).append(matching_options)
    
    return JsonResponse({
        'deposit_products': products_data.data,
    }, json_dumps_params={'ensure_ascii': False})