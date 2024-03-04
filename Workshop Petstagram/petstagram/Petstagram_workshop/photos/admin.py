from django.contrib import admin

from Petstagram_workshop.photos.models import Photo, Comment, Like


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'modified_on', 'description', 'pets_tagged')

    @staticmethod
    def pets_tagged(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('to_photo',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('to_photo', 'added_on')


