from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from .forms import PetstagramUserCreationForm, PetstagramChangeForm
from .models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class PetstagramUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    add_form = PetstagramUserCreationForm
    form = PetstagramChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'date_of_birth']
