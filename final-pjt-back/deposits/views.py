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
        fin_prdt_cd = option.get('fin_prdt_cd')
        deposit_product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=deposit_product.pk)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def deposit_products(request):
    if request.method == "GET":
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
