from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/delete/', views.article_delete),
    path('<int:article_pk>/comments/', views.comment_list),
    path('<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/likes/', views.likes),
    
]
 