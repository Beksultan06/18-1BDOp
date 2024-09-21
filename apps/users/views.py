from django.shortcuts import render
# from rest_framework.generics import ListAPIView, CreateAPIView
from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer
# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

# class UserAPIView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserRegisterAPIView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer

class UserRegisterAPI(GenericViewSet,
                      ListModelMixin,
                      CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer