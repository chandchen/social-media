from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from users.models import Profile


class UserCreateSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=100, help_text='Required')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserProfileSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user',
            'photo',
            'gender',
            'bio',
            'location',
            'birthday',
            'website',
        ]

    def get_photo(self, obj):
        try:
            photo = obj.photo.url
        except:
            photo = None
        return photo
