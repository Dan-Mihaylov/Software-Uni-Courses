from django.contrib import admin

from MusicApp.account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass