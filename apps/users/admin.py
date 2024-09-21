from django.contrib import admin
from apps.users.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'email', 'is_active', 'phone_number')
    list_editable = ('is_active', )
    list_filter = ('username', 'is_active',)
    search_fields = ('username', 'is_active',)