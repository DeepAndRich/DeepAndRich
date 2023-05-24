from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
import requests
from .serializers import ExchangeRateSerializer
from rest_framework.response import Response
from .models import ExchangeRateInfo
from django.http import JsonResponse

# BASE_URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON/'
API_KEY = settings.API_KEY_2

@api_view(['GET'])
def save_exchange_rate(request):
  URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON/'
  params = {
    'authkey': API_KEY,
    'searchdate': '20230524',
    'data' : 'AP01'
  }
  response = requests.get(URL, params=params)
  info_list = response.json()
  for info in info_list:
    info_data = {
      'cur_unit' : info.get('cur_unit'),
      'cur_nm' : info.get('cur_nm'),
      'deal_bas_r' : info.get('deal_bas_r')
    }
    serializer = ExchangeRateSerializer(data=info_data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()

  return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def view_exchange_rate(request):
  print('dd')
  info_dummy = ExchangeRateInfo.objects.all()
  print(info_dummy)
  info_list = []
  for info in info_dummy:
    info_data = {
      'cur_unit' : info.cur_unit,
      'cur_nm' : info.cur_nm,
      'deal_bas_r' : info.deal_bas_r,
    }
    info_list.append(info_data)
  return JsonResponse(info_list, safe=False)

