from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from apps.news.models import News
from apps.news.serializers import NewsSerializers
from apps.news.filters import NewsFilter
# Create your views here.
class NewsAPI(GenericViewSet,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.ListModelMixin,
              mixins.DestroyModelMixin, 
              PageNumberPagination):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'is_active']
    search_fields = ['title']
    filter_class = NewsFilter
    # page_size = 3
    # max_page_size = 10