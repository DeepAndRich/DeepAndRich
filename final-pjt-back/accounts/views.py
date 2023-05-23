from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from deposits.models import DepositProducts



@api_view(['POST'])
def save_product(request, product_pk):
    user_id = request.POST.get('user_id')
    product = get_object_or_404(DepositProducts, pk=product_pk)
    
    user = get_object_or_404(User, pk=user_id)
    user.sub_product.add(product)
    # 필요한 경우 응답을 반환할 수 있습니다.
    return JsonResponse({'message': 'Product saved successfully!'})
  
# def subscribe(request, user_pk):
#   User = User.objects.all()
#   product = User.objects.get(pk=user_pk)
#   if product != request




# @api_view(['GET'])
# def deposit_products(request, month_pk):
#     a1 = DepositOptions.objects.select_related('fin_prdt_cd')
#     a2 = a1.filter(save_trm=month_pk).order_by('-intr_rate')

#      # 직렬화된 a2 데이터 생성
#     a2_data = DepositOptionsProductsSerializer(a2, many=True).data

#     return JsonResponse(a2_data, safe=False)