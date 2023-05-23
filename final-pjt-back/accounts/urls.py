from django.urls import path, include
from . import views

urlpatterns = [
    # path('<int:user_pk>/subscribe/', views.subscribe)
    path('save-product/<int:fin_prdt_cd>', views.save_product),

 
]
