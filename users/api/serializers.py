from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
)

from users.models import Profile


class UserListSerializer(ModelSerializer):
    detail = HyperlinkedIdentityField(view_name='users-api:detail')
    email = serializers.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'detail',
        ]
        read_only_fields = [
            'first_name',
            'last_name',
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
        validated_data['id'] = user_obj.id
        return validated_data


class ProfileDetailSerializer(ModelSerializer):

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
        read_only_fields = [
            'user',
        ]


class UserDetailSerializer(HyperlinkedModelSerializer):
    profile = ProfileDetailSerializer(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
        ]
        read_only_fields = [
            'id',
            'username',
            'email',
        ]

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile.photo = profile_data.get('photo', profile.photo)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.location = profile_data.get('location', profile.location)
        profile.birthday = profile_data.get('birthday', profile.birthday)
        profile.website = profile_data.get('website', profile.website)
        profile.save()

        return instance


class UserCreateSerializer(ModelSerializer):
    email = serializers.EmailField(label='Email Address')

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


class UserLoginSerializer(ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        username = data['username']
        password = data['password']
        user = User.objects.filter(username=username)
        if user.exists():
            user_obj = User.objects.get(username=username)
            if user_obj.check_password(password):
                return data
            else:
                raise serializers.ValidationError(
                    "Username and password doesn't match!")
        else:
            raise serializers.ValidationError(
                "User do not exists!")
