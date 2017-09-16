from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from rest_framework import serializers

from users.models import Profile


class UserListSerializer(ModelSerializer):
    detail = HyperlinkedIdentityField(view_name='users-api:detail')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'detail',
        ]


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


class UserDetailSerializer(ModelSerializer):
    profile = ProfileDetailSerializer()

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

        profile.photo = validated_data.get('photo', profile.photo)
        profile.bio = validated_data.get('bio', profile.bio)
        profile.location = validated_data.get('location', profile.location)
        profile.birthday = validated_data.get('birthday', profile.birthday)
        profile.website = validated_data.get('website', profile.website)
        profile.save()

        return instance


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
