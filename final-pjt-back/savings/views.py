from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.shortcuts import get_object_or_404
from .models import SavingProducts, SavingOptions
from .serializers import SavingProductsSerializer, SavingOptionsSerializer, SavingOptionsProductsSerializer
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
def saving_products(request, month_pk):
  
    a1 = SavingOptions.objects.select_related('fin_prdt_cd')
    a2 = a1.filter(save_trm=month_pk).order_by('-intr_rate')
    a3 = SavingOptions.objects.all()

     # 직렬화된 a2 데이터 생성
    a2_data = SavingOptionsProductsSerializer(a2, many=True).data


    return JsonResponse(a2_data, safe=False)
 
@api_view(['GET'])
def freestyle(request):
    a1 = SavingOptions.objects.select_related('fin_prdt_cd')
    a2 = a1.filter(save_trm=6).order_by('-intr_rate')[:10]
    a3 = a1.filter(save_trm=12).order_by('-intr_rate')[:10]

    a2_data = SavingOptionsProductsSerializer(a2, many=True).data
    a3_data = SavingOptionsProductsSerializer(a3, many=True).data
    combined_data = a2_data + a3_data
    sorted_data = sorted(combined_data, key=lambda x: x['intr_rate'], reverse=True)
    
    unique_data = []
    unique_prdt_cd = []
    for item in sorted_data:
        if item['fin_prdt_cd'] not in unique_prdt_cd:
            unique_data.append(item)
            unique_prdt_cd.append(item['fin_prdt_cd'])

    return JsonResponse(sorted_data[:5], safe=False)



@api_view(['GET'])
def breaststroke(request):
    a1 = SavingOptions.objects.select_related('fin_prdt_cd')
    a2 = a1.filter(save_trm=24).order_by('-intr_rate')[:10]
    a3 = a1.filter(save_trm=36).order_by('-intr_rate')[:10]

    a2_data = SavingOptionsProductsSerializer(a2, many=True).data
    a3_data = SavingOptionsProductsSerializer(a3, many=True).data
    combined_data = a2_data + a3_data
    sorted_data = sorted(combined_data, key=lambda x: x['intr_rate'], reverse=True)

    unique_data = []
    unique_prdt_cd = []
    for item in sorted_data:
        if item['fin_prdt_cd'] not in unique_prdt_cd:
            unique_data.append(item)
            unique_prdt_cd.append(item['fin_prdt_cd'])

    return JsonResponse(sorted_data[:5], safe=False)