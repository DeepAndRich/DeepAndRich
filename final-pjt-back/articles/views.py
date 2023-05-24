from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# from drf_yasg.utils import swagger_auto_schema

# Create your views here.
# @swagger_auto_schema(methods=['POST'], request_body=ArticleListSerializer)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        if request.user.is_authenticated:
            serializer = ArticleListSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                author = request.user
                serializer.save(author=author)
              
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'message': 'Invalid'})
        return JsonResponse({'message':'Not allowed'})



@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['DELETE'])
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            message = 'disliked'
        else:
            article.like_users.add(request.user)
            message = 'liked'
        return Response({'message': message})
    return JsonResponse({'message': 'Not allowed'})