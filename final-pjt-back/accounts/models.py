from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from allauth.account.adapter import DefaultAccountAdapter
from deposits.models import DepositProducts
from savings.models import SavingProducts

class User(AbstractUser):
    realname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    asset = models.IntegerField()
    region = models.CharField(max_length=20)
    personal_type = models.CharField(max_length=30, null=True)
    sub_deposit_product = models.ManyToManyField(DepositProducts, symmetrical=False, blank=True)
    sub_saving_product = models.ManyToManyField(SavingProducts, symmetrical=False, blank=True)
    # user_img = models.ImageField(upload_to='images/', null=True)

    # def __str__(self):
    #     return str(self.title)


# 상속 받아서 구현해보기

class CustomAccountAdapter(DefaultAccountAdapter):
    # 기본 코드는 다 그대로 쓰고, save_user 만 오버라이딩 하겠다!
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        # nickname 필드
        nickname = data.get("nickname")
        age = data.get("age")
        asset = data.get("asset")
        region = data.get("region")
        realname = data.get("user_id")
        

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        # 닉네임 필드 추가
        if nickname:
            user_field(user, "nickname", nickname)
        if age:
            user.age = age
        if asset:
            user.asset = asset
        if region:
            user_field(user, "region", region)
        if realname:
            user_field(user, "user_id", realname)
     
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            pass
            user.save()
        return user

