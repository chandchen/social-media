from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
)

from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserLoginSerializer,
)
from .pagination import UsersPagination


class UserListAPIView(ListCreateAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    pagination_class = UsersPagination

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data, context={'request': request})
    #     if serializer.is_valid(raise_exception=True):
    #         return Response(serializer.data, status=HTTP_200_OK)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'pk'

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.kwargs.get('pk'))


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def get(self, request, *args, **kwargs):
        return Response('Welcome to chand api view, please login first!')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            if user.is_active:
                login(request, user)
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
