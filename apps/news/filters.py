import django_filters
from apps.news.models import News, CategoryNews

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = News
        fields = ['title', 'is_active']