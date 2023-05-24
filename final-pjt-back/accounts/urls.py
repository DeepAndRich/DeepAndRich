from django.urls import path, include
from . import views

urlpatterns = [
    # 저장 / 삭제
    path('save-deposit-myproduct/<int:product_pk>/', views.save_deposit_myproduct),
    path('save-saving-myproduct/<int:product_pk>/', views.save_saving_myproduct),
    # 조회
    path('<int:user_pk>/myproduct/', views.myproduct),
    # path('<int:user_pk>/saving-myproduct/', views.saving_myproduct),
    # path('<int:user_pk>/user_img/', views.user_img),
]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
