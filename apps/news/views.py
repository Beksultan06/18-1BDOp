from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from apps.news.models import News
from apps.news.serializers import NewsSerializers
# Create your views here.
class NewsAPI(GenericViewSet,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.ListModelMixin,
              mixins.DestroyModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializers