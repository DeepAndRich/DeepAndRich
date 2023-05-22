from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    realname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=50)
    age = models.IntegerField()
    asset = models.IntegerField()
    region = models.CharField(max_length=20)
    personal_type = models.CharField(max_length=10, null=True)
    sub_proudct = models.CharField(max_length=50, null=True)

# 상속 받아서 구현해보기
from allauth.account.adapter import DefaultAccountAdapter

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
            user_field(user, "user_id", user_id)
     
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # 비밀번호 수정
            if 'password1' in data:
                password = data['password1']
                user.set_password(password)
            
            # 자산 수정
            if 'asset' in data:
                asset = data['asset']
                user.asset = asset

            # 나이 수정
            if 'age' in data:
                age = data['age']
                user.age = age
            
            # 닉네임 수정
            if 'nickname' in data:
                nickname = data['nickname']
                user.nickname = nickname
            
            # 가입상품 항목 수정
            if 'personal_type' in data:
                personal_type = data['personal_type']
                user.personal_type = personal_type
            user.save()
        return user