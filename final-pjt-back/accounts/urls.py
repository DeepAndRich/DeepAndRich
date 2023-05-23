from django.urls import path, include
from . import views

urlpatterns = [
    # path('<int:user_pk>/subscribe/', views.subscribe)
    path('save-product/<int:product_pk>', views.save_product),

 
]
