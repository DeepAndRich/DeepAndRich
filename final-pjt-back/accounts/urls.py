from django.urls import path
from . import views

urlpatterns = [
    # path('test/', views.test),

    # path('user_update/', views.user_update),
    path('user_profile/', views.user_profile),
    # path('login/', views.login),
]
