from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.user import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'full_name',
        )}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_verified', 'is_superuser',
                'groups', 'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'full_name',
                'password1',
                'password2',
            ),
        }),
    )
    ordering = ('-id',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_verified', 'groups')
    search_fields = ('full_name', 'email')
    list_display_links = ('email',)
