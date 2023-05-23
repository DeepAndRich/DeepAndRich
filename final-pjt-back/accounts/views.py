from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def save_product(request, fin_prdt_cd):
  User = User.objects.all()
  fin_prdt_cd = request.get('fin_prdt_cd')

  
# def subscribe(request, user_pk):
#   User = User.objects.all()
#   product = User.objects.get(pk=user_pk)
#   if product != request