from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer, UserProfileSerializer, UserListSerializer, UserDetailSerializer

from users.models import Profile


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.kwargs.get('pk'))


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [AllowAny]
