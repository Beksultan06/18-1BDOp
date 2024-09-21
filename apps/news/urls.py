from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.news.views import NewsAPI

router = DefaultRouter()
router.register('news', NewsAPI, basename='news')

urlpatterns = [

]

urlpatterns += router.urls