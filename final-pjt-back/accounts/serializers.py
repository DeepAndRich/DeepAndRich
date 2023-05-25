from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from allauth.utils import email_address_exists, get_username_max_length
from allauth.account import app_settings as allauth_account_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.utils.translation import gettext_lazy as _
from .models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
        required=allauth_account_settings.USERNAME_REQUIRED,
    )
    email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    realname = serializers.CharField(max_length=30)
    nickname = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    asset = serializers.IntegerField()
    region = serializers.CharField(max_length=20)
 
   
    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _('A user is already registered with this e-mail address.'),
                )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        user.nickname = self.cleaned_data.get('nickname', None)
        user.age = self.cleaned_data.get('age', None)
        user.asset = self.cleaned_data.get('asset', None)
        user.region = self.cleaned_data.get('region', None)
        user.save()

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'realname' : self.validated_data.get('user_id',''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', ''),
            'asset': self.validated_data.get('asset', ''),
            'region': self.validated_data.get('region', ''),
            

        }

    def save(self, request):
        # allauth 의 기본 adaper 를 가져옴
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        # 기본 adaper 의 save_user 는 nickname 필드를
        # 저장하지 않는다!
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.personal_type = self.cleaned_data.get('personal_type', None)
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user




class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk','realname','age','nickname','asset','region', 'personal_type',
        )
        read_only_fields = ('pk',)