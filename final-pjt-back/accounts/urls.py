from django.urls import path, include
from . import views

urlpatterns = [
    # 저장 / 삭제
    path('save_myproduct/<int:product_pk>/', views.save_myproduct),
    # 조회
    path('<int:user_pk>/myproduct/', views.myproduct),
]
