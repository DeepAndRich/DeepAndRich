from django.urls import path
from . import views

urlpatterns = [
    # path('api_test/', views.api_test),
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/<int:month_pk>/', views.deposit_products),
    path('backstroke/', views.backstroke),
    path('butterfly/', views.butterfly)
]