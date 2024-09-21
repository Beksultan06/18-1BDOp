from rest_framework import serializers
from apps.news.models import News

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'