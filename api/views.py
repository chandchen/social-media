# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from .serializers import UserSerializer, ProfileSerializer
#
# from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
#
# from users.models import Profile
#
#
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileAPIView(APIView):
#
#     def get(self, request, format=None):
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)
#
#
# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world"})
#
#
# class UsersViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         context = {'request': request}
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, context=context, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import UserSerializer, PostSerializer, PhotoSerializer
from .models import User, Post, Photo


class UserMixin(object):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(UserMixin, generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(UserMixin, generics.RetrieveAPIView):
    lookup_field = 'username'


class PostMixin(object):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Force author to the current user on save"""
        serializer.save(author=self.request.user)


class PostList(PostMixin, generics.ListCreateAPIView):

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class PostDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class UserPostList(generics.ListAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


class PhotoMixin(object):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoList(PhotoMixin, generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class PhotoDetail(PhotoMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class PostPhotoList(generics.ListAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(PostPhotoList, self).get_queryset()
        return queryset.filter(post__pk=self.kwargs.get('pk'))


"""***************************************************************"""

from django.shortcuts import get_object_or_404, redirect
from users.models import Profile
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, LoginSerializer

from django.contrib.auth import login, authenticate
from django.views.generic.base import View
from django.shortcuts import render, HttpResponseRedirect


class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/profile_list.html'

    def get(self, request):
        queryset = Profile.objects.all()
        return Response({'profiles': queryset})


class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('api:profile-list')


# class LoginView(View):
#
#     def get(self, request):
#         return render(request, 'api/login.html')
#
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user.is_active:
#             login(request, user)
#             return HttpResponseRedirect('/api/profile/')
#         return render(request, 'api/login.html')


class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/login.html'
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/api/profile/')
            else:
                return render(request, 'api/login.html')
        else:
            return render(request, 'api/login.html')
