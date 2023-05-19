from django.urls import path
from . import views

urlpatterns = [
    # path('api_test/', views.api_test),
    path('save_saving_products/', views.save_saving_products),
    path('saving-products/', views.saving_products),
]