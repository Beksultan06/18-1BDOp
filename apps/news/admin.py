from django.contrib import admin

from apps.news.models import News

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_editable = ('is_active', )
    list_display = ('title', 'is_active')