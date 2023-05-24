from django.urls import path
from . import views

urlpatterns = [
    # path('api_test/', views.api_test),
    path('save-saving-products/', views.save_saving_products),
    path('saving-products/<int:month_pk>/', views.saving_products),
    path('freestyle/', views.freestyle),
    path('breaststroke/', views.breaststroke)
]