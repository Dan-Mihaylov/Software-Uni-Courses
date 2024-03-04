from django.contrib import admin
from Petstagram_workshop.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_of_birth', 'slug']
