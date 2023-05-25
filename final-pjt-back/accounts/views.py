from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from deposits.models import DepositProducts
from savings.models import SavingProducts


@api_view(['POST'])
def save_deposit_myproduct(request, product_pk):
  if request.user.is_authenticated:
    user = request.user
    product = DepositProducts.objects.get(pk=product_pk)
    if user.sub_deposit_product.filter(pk=product.pk).exists():
      user.sub_deposit_product.remove(product)
    else:
      user.sub_deposit_product.add(product)
    return JsonResponse({'message': 'Product saved successfully!'})
  return JsonResponse({'message' : 'Not allowed'})



@api_view(['POST'])
def save_saving_myproduct(request, product_pk):
  if request.user.is_authenticated:
    user = request.user
    product = SavingProducts.objects.get(pk=product_pk)
    if user.sub_saving_product.filter(pk=product.pk).exists():
      user.sub_saving_product.remove(product)
    else:
      user.sub_saving_product.add(product)
    return JsonResponse({'message': 'Product saved successfully!'})
  return JsonResponse({'message' : 'Not allowed'})



@api_view(['GET'])
def myproduct(request, user_pk):
  user = User.objects.get(pk=user_pk)
  sub_deposist_products = user.sub_deposit_product.all()
  
  sub_products_list = []
  if sub_deposist_products:
    for sub_product in sub_deposist_products:
      sub_product_data = {
        'id' : sub_product.pk,
        'fin_prdt_cd': sub_product.fin_prdt_cd,
        'kor_co_nm' : sub_product.kor_co_nm,
        'fin_prdt_nm': sub_product.fin_prdt_nm,
      }
      sub_products_list.append(sub_product_data)
  sub_saving_products = user.sub_saving_product.all()
  if sub_deposist_products:
    for sub_product in sub_saving_products:
      sub_product_data = {
        'id' : sub_product.pk,
        'fin_prdt_cd': sub_product.fin_prdt_cd,
        'kor_co_nm' : sub_product.kor_co_nm,
        'fin_prdt_nm': sub_product.fin_prdt_nm,
      }
      sub_products_list.append(sub_product_data)
  return JsonResponse(sub_products_list, safe=False)



# @api_view(['POST'])
# def user_img(request, user_pk):
#   image = User.user_img