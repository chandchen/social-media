from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import Profile


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ('user', 'gender', 'bio', 'location', 'birthday', 'website')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=100,
        style={'placeholder': 'Username', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('id', 'username', )



"""***************************************************"""


from rest_framework import serializers

from .models import User, Post, Photo


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField(view_name='api:userpost-list', lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts', )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    photos = serializers.HyperlinkedIdentityField(view_name='api:postphoto-list')

    class Meta:
        model = Post
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = Photo
        fields = '__all__'
