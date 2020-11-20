from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import GivenDevice

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'surname', 'is_active']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    list_editable = ['name', 'surname', 'is_active']
    search_fields = ['name', 'surname', 'email', 'device__device_model']


admin.site.register(GivenDevice)
