from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# @api_view(['GET'])
# def test(request):
#     return JsonResponse({ 'message': 'okay' })



@api_view(['GET', 'PUT'])
def user_profile(request):

  if request.method == 'GET':
      view = UserDetailsView.as_view()
      response = view(request._request)
      return response
  elif request.method == 'PUT':
    serializer = RegisterSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

