from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from deposits.models import DepositProducts



@api_view(['POST'])
def save_myproduct(request, product_pk):
  if request.user.is_authenticated:
    user = request.user
    product = DepositProducts.objects.get(pk=product_pk)
    if user.sub_product.filter(pk=product.pk).exists():
      user.sub_product.remove(product)
    else:
      user.sub_product.add(product)

    return JsonResponse({'message': 'Product saved successfully!'})
  return JsonResponse({'message' : 'Not allowed'}, status=401)


@api_view(['GET'])
def myproduct(request, user_pk):
  user = User.objects.get(pk=user_pk)
  sub_products = user.sub_product.all()
  print(sub_products)
  sub_products_list = []
  for sub_product in sub_products:
    sub_product_data = {
      'id' : sub_product.pk,
      'fin_prdt_cd': sub_product.fin_prdt_cd,
      'kor_co_nm' : sub_product.kor_co_nm,
      'fin_prdt_nm': sub_product.fin_prdt_nm,
    }
    sub_products_list.append(sub_product_data)
  return JsonResponse(sub_products_list, safe=False)




# @api_view(['GET'])
# def deposit_products(request, month_pk):
#     a1 = DepositOptions.objects.select_related('fin_prdt_cd')
#     a2 = a1.filter(save_trm=month_pk).order_by('-intr_rate')

#      # 직렬화된 a2 데이터 생성
#     a2_data = DepositOptionsProductsSerializer(a2, many=True).data

#     return JsonResponse(a2_data, safe=False)