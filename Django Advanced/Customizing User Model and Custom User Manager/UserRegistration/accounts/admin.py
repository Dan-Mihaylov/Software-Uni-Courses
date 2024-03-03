from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active']

    # When you are changing the password on the user
    fieldsets = (
        (
            None, {
            'fields': ('email', 'password')
        }),
        (
            'Permissions', {
                'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')
            }
        ),

    )

    # When you are creating a new user
    add_fieldsets = (
        (
            None, {
                'classes': ('wide'),
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions')
            },
        ),
    )

    search_fields = ['email']

    ordering = ['email']


