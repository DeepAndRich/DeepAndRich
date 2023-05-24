from django.urls import path
from . import views

urlpatterns = [
    path('save-exchange-rate/', views.save_exchange_rate),
    path('view-exchange-rate/', views.view_exchange_rate),
]

